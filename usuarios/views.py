from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UsuarioSerializer
from rest_framework.permissions import IsAdminUser

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdminUser]
    
    class Meta:
        model=User
        