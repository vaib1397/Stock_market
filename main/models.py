from django.db import models
from Stock_Market.mixins import Timestampedmodel
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser, Timestampedmodel):
    username = models.CharField(max_length=56, unique=True)
    email = models.EmailField(max_length=155, blank=True, null=True)

    USERNAME_FIELD = 'username'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Stock(models.Model):
    NSE = 'nse'
    BSE = 'bse'
    REGISTERED_AT = (
        (NSE,NSE),
        (BSE,BSE)
    )
    stock_name = models.CharField(max_length=15)
    open_price = models.FloatField(null=True, blank=True)
    close_price = models.FloatField(null=True, blank=True)
    upper_circuit = models.FloatField(null=True, blank=True)
    lower_circuit = models.FloatField(null=True, blank=True)
    registered_at = models.CharField(max_length=50, choices=REGISTERED_AT, null=True, blank=True)


class Stockdetail(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    video = models.SlugField(max_length=50, null=True, blank=True)
    detail = models.OneToOneField(Stock, on_delete=models.CASCADE)


admin.site.register(User)
admin.site.register(Stock)
admin.site.register(Stockdetail)
