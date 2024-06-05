from msilib.schema import ListView

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from e_wallet.models import Wallet
from user_.models import CircularUser
from e_wallet.serializers import WalletDetailSerializer


class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletDetailSerializer
    permission_classes = (IsAuthenticated,)


def find_wallet(username):
    try:
        user = CircularUser.objects.get(username=username)
        wallet = Wallet.objects.get(user=user)
        return wallet
    except (CircularUser.DoesNotExist, Wallet.DoesNotExist):
        return None

