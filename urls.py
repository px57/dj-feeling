"""
    @description: This file contains the urls for the profiles app
"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        'load/', 
        views.load, 
        name='feeling__load'
    ),
    path(
        'like/', 
        views.like, 
        name='feeling__like'
    ),
    path(
        'dislike/', 
        views.dislike, 
        name='feeling__dislike'
    ),
]