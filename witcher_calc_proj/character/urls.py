from django.urls import path
from .views import CharactersList, CharactersCreate, CharacterUpdateDestroy, CharacterDetailsView

app_name = 'characters'
urlpatterns = [   
    path('list/', CharactersList.as_view(), name='char-list'),
    path('create/', CharactersCreate.as_view(), name='char-create'),
    path('details/<slug>/', CharacterDetailsView.as_view(), name='char-details'),
    path('update/<slug>/', CharacterUpdateDestroy.as_view(), name='char-update')
]