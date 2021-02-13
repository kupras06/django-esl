
from django.contrib import admin
from django.urls import path, re_path,include  # add this
from django.views.generic import TemplateView
import esl.views as esl_views
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('home/',esl_views.home,name='home'),
    path('',esl_views.home,name='home'),
    path('about/',esl_views.about,name='about'),
    path('accounts/', include('allauth.urls')),
    path('<str:username>/', include('esl.urls')),
]
