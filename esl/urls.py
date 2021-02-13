# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('dashboard', views.index, name='dashboard'),
    path('profile/', views.profile, name='user_profile'),
    path('create-event/', views.createEvent    , name='create_event'),

    path('register/', views.register , name='register'),
]
