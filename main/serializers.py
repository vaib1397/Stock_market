import imp
from multiprocessing import AuthenticationError

from django.forms import ValidationError
from main.models import Stockdetail, User, Stock
from rest_framework import serializers
from django.contrib.auth import authenticate, login
from rest_framework import exceptions

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password','first_name']



class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class StockdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stockdetail
        fields = '__all__'

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name')
        extra_kwargs = {'password': {'write_only':True}}

        def create(self, validated_data):
            user = User.objects.create_user(validated_data['username'], validated_data['password'])

            return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = authenticate(username=username,password=password)

            if user:
                if user.is_active:
                    data["user"]=user
                else:
                    msg = "user is deactivated"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password"
            raise exceptions.ValidationError(msg)
        return data
