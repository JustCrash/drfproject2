from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from users.serializers import UserSerializer
from users.models import User

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
