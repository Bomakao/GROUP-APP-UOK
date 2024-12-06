from django.urls import path
from .views import create_groups

urlpatterns = [
    path('create-groups/', create_groups, name='create-groups'),
]
