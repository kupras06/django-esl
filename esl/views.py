from django.shortcuts import render

# Create your views here.
# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
# import simplejson as json
from django.conf.urls import url
import requests
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .forms import *
from esl.models import Profile, Tournament, Result
from django.contrib.auth.models import User
import datetime


@login_required(login_url="/account/login")
def index(request, username):
    if request.method=='POST':
        id = request.POST.get('id')
        print(id)
        Tournament.objects.filter(id=id).delete()
    print(request.method)
    user = User.objects.filter(username=request.user)
    # print(user)
    host = Tournament.objects.filter(creator=request.user)
    # print(host)
    register = Result.objects.filter(user=request.user)
    return render(request, "dashboard.html", {'host': host, 'reg': register})


@login_required
def profile(request, username):
    print(request.method)
    if request.method=='POST':
        temp = Profile.objects.get(user=request.user)
        print(request.POST.get('new-address'))
        temp.address = request.POST.get('new-address')
        temp.city = request.POST.get('new-city')
        temp.country = request.POST.get('new-country')
        temp.state = request.POST.get('new-state')
        temp.pin_code = request.POST.get('new-pin')

        temp.state = request.POST.get('new-state')
        temp.save()
        # temp.address =
    data = {}
    data["user"] = request.user
    data["email"] = request.user.email
    data['image'] = " static 'assets/img/brand/esl.svg'"
    # if request.user.socialaccount_set.all.0.get_avatar_url:
    #     data['image'] = request.user.socialaccount_set.all.0.get_avatar_url
    data["first_name"] = request.user.first_name
    data["last_name"] = request.user.last_name
    profile = Profile.objects.get(user=request.user)
    # print(profile.address)
    data["address"] = profile.address
    data["city"] = profile.city
    data["country"] = profile.country
    data["pin"] = profile.pin_code
    data["dob"] = profile.birth_date
    data['state'] = profile.state
    # print(request.user.email)
    # print(request.method)
    form = EditUserForm()
    return render(request, "profile.html", {"data": data, 'form': form})


@login_required
def createEvent(request, username):
    if request.method == "POST":
        print(request.POST)
        print(request.user)
        tour = Tournament()
        data = dict(request.POST)
        tour.creator = request.user
        tour.game_name = data.get("game_name")[0]
        tour.event_name = data.get("event_name")[0]
        tour.end_date = data.get("registration_starts")[0]
        tour.save()

    form = CreateEventForm()
    return render(request, "create-event.html", {'form': form})


@login_required
def register(request, username):
    if request.method == "POST":
        print(request.POST)
        print(request.user)
        tour = Result()
        tour.user = request.user
        data = dict(request.POST)
        print(data['id'])

        curEvent = Tournament.objects.get(id=data['id'][0])
        tour.event = curEvent
        tour.position = 0

        if (tour.user == curEvent.creator):
            print("HOST CANNOT REGISTER")
        else:
            tour.save()
    events = Tournament.objects.all()
    print(events)
    return render(request, "register.html", {'form': events})

def home(request):
    return render(request,'home.html')



def about(request):
    return render(request,'about.html')