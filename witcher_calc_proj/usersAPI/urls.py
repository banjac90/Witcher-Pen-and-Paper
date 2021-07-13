from django.urls import path, include
from .views import UserUpdateView, UserDetailView, UserDestroyView, ListUsersView, RegistrationView

app_name = 'user'
urlpatterns = [    
    path('list/', ListUsersView.as_view(), name = 'user-list'),
    path('update/<slug>/', UserUpdateView.as_view(), name = 'user-update'),
    path('detail/<slug>/', UserDetailView.as_view(), name = 'user-detail'),
    path('delete/<slug>/', UserDestroyView.as_view(), name = 'user-delete'),
    path('Registration/', RegistrationView.as_view(), name = 'user-register'),
    #path('test/', ExampleView.as_view(), name = 'test'),
    path('auth', include('rest_framework.urls') ),
]