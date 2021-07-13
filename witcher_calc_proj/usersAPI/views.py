from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, ListCreateAPIView, CreateAPIView
from .serializers import UserDetailSerializer, RegistrationSerializer
from .models import User
from rest_framework.permissions import AllowAny

class ListUsersView(ListCreateAPIView):
   queryset = User.objects.all()
   serializer_class = UserDetailSerializer

class UserUpdateView(RetrieveUpdateAPIView):
   queryset = User.objects.all() 
   serializer_class = UserDetailSerializer
   lookup_field = 'slug'

class UserDetailView(RetrieveAPIView):
   queryset = User.objects.all() 
   serializer_class = UserDetailSerializer
   lookup_field = 'slug'

class UserDestroyView(DestroyAPIView):
   queryset = User.objects.all() 
   serializer_class = UserDetailSerializer
   lookup_field = 'slug'

class RegistrationView(CreateAPIView):   
   serializer_class = RegistrationSerializer
   permission_classes = [AllowAny]
