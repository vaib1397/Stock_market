import django
from django.shortcuts import render, get_object_or_404
from main.serializers import LoginSerializer, SignupSerializer, UserSerializer, StockdetailSerializer, StockSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from main.models import User, Stock,Stockdetail
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import mixins, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.contrib.auth import login as django_login, logout as django_logout
from .utils import LimitSetPagination

class UserListView(APIView, mixins.ListModelMixin):

    authentication_class = (TokenAuthentication)
    permission_class = (IsAuthenticated, )
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        if not "pk" in kwargs:
            return self.list(request)
        post = get_object_or_404(User, pk=kwargs["pk"])
        return Response(UserSerializer(post).data, status=200)


class StocklistView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = StockSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = ()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['stock_name']
    queryset = Stock.objects.all()
    pagination_class = LimitSetPagination

    def get(self, request, *args, **kwargs):
        if not "pk" in kwargs:
            return self.list(request)
        post = get_object_or_404(Stock, pk=kwargs["pk"])
        return Response(StockSerializer(post).data, status=200)

    def post(self, request):
        data = request.data
        serializer = StockSerializer(data=data)
        if serializer.is_valid():
            post = serializer.save()
            return Response(StockSerializer(post).data, status=201)
        return Response(serializer.errors, status=400)


class SignupView(generics.GenericAPIView):
    serializer_class = SignupSerializer
    permission_classes = (AllowAny, )
    authentication_classes = ()

    def post(self,request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"user" : UserSerializer(user, context=self.get_serializer_context()).data,
        "token": Token.objects.create(user)[1]})


class LoginView(APIView):
    permission_classes = (AllowAny, )

    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=200)