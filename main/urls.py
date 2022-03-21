from django.urls import path

from .views import *

urlpatterns = [
    path('users', UserListView.as_view()),
    path('stock', StocklistView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('signup', SignupView.as_view()),
]