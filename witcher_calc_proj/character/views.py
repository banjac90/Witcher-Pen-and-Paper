from .models import Character
from .serializers import UpdateDetailsCharacterSerializer, CreateCharacterSerializer, listCharacterSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView

class CharactersList(ListAPIView):
    queryset = Character.objects.all()
    serializer_class = listCharacterSerializer

class CharactersCreate(CreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CreateCharacterSerializer

class CharacterUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()    
    serializer_class = UpdateDetailsCharacterSerializer
    lookup_field = 'slug'

class CharacterDetailsView(RetrieveAPIView):
    queryset = Character.objects.all()    
    serializer_class = UpdateDetailsCharacterSerializer
    lookup_field = 'slug'