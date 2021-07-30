from django.shortcuts import render, HttpResponse, redirect
from home.models import Video, Category
from django.contrib import messages
# copy and past
# from .forms import ProfileModelForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# copy and past

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login, logout
from django.db import models
from .models import Video
from math import ceil


def Videos(request):
    video = Video.objects.all()
    cats = Category.objects.all()
    context = {"video": video, "cats": cats, }
    return render(request, "home/Videos.html", context)


# Create your views here.
def Whenplay(request, Video_id):
    Videos = Video.objects.filter(Video_id=Video_id).first()
    Videos.views = Videos.views + 101
    Videos.save()
    cats = Category.objects.all()
    # these is for the filtering   the video name descripitons and tags categorys and fach to the templates
    # query = str(
    #     f"{Videos.Category}, {Videos.Video_name}, {Videos.Desc},{ Videos.Tages}")
    # catprods = Video.objects.values('Category', 'Video_id')
    # print(f'these is the category:{catprods}')
    query = str(Videos.Category)
    All_Video_name = Video.objects.filter(Video_name__icontains=query)
    All_Video_category = Video.objects.filter(Category__icontains=query)
    All_Video_desc = Video.objects.filter(Desc__icontains=query)
    All_Video_tags = Video.objects.filter(Tages__icontains=query)

    RelatedVidoes = All_Video_name.union(
        All_Video_category, All_Video_desc, All_Video_tags)
    context = { "Videos": Videos,  "RelatedVidoes": RelatedVidoes,"cats": cats, }
    return render(request, "home/whenplay.html", context)


def channel(request, Username):
    susers = ShareitsUser.objects.filter(Username=Username)
    # susers = ShareitsUser.objects.all()
    video = Video.objects.all()
    context = {"video": video, "susers": susers}
    return render(request, "home/channel.html", context)


def search(request):
    query = request.GET['query']
    if len(query) > 78:
        video = Video.objects.none()
    else:
        Video_name = Video.objects.filter(Video_name__icontains=query)
        Category = Video.objects.filter(Category__icontains=query)
        Desc = Video.objects.filter(Desc__icontains=query)
        Tages = Video.objects.filter(Tages__icontains=query)
        video = Video_name.union(Tages, Category, Tages, Desc)
    if video.count() == 0:
        messages.warning(
            request, "No search results found. Please refine your query.")
    params = {'video': video, 'query': query}
    return render(request, 'home/search.html', params)

# authaundactions starts


def signup(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        # pass2 = request.POST['pass2']

        # check for errorneous input
        if len(username) <= 8:
            messages.error(
                request, " Your user name must be under 10 characters")
            return redirect('Home')

        if not username.isalnum():
            messages.error(
                request, " User name should only contain letters and numbers")
            return redirect('Home')
        # if (pass1 != pass2):
        #     messages.error(request, " Passwords do not match")
        #     return redirect('home')

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(
            request, " Your Shareits has been successfully created")
        return redirect('Home')

    else:
        return HttpResponse("404 - Not found")


def handeLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(
                request, f"Successfully Logged In  {{request.user}}")
            return redirect("Home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("Home")

    return HttpResponse("404- Not found")
    return HttpResponse("login")


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('Home')
