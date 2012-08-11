from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Video
from .forms import VideoForm


def home(request):
    "home page"
    videos = Video.objects.all().order_by('-view_count')
    return render(request, "home.html",
            {"videos": videos})


@login_required
def upload(request):
    "upload page"
    if request.POST:
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            messages.info(request, "Upload success")
            return redirect("/")
    else:
        form = VideoForm()
    return render(request, "upload.html",
                {"form": form})


def view(request, video_id):
    "view video"
    video = get_object_or_404(Video, id=video_id)
    video.increment_view()
    return render(request, "view.html",
            {"video": video})


def login_user(request, *args, **kwargs):
    "login page"
    result = login(request, *args, **kwargs)
    return result


def register_user(request):
    "register page"
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.info(request, "User %s created, please log in" % user)
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "register.html",
                    {"form": form})
