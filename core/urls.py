from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

import esl.views as esl_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", esl_views.home, name="home"),
    path("app/", esl_views.home, name="home"),
    path("about/", esl_views.about, name="about"),
    path("", TemplateView.as_view(template_name="svelte.html"), name="svelte_app"),
    path("accounts/", include("allauth.urls")),
    path("<str:username>/", include("esl.urls")),
]
