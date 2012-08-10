from django.shortcuts import render, get_object_or_404, redirect
from .models import Video


def home(request):
    "home page"
    videos = Video.objects.all().order_by('-view_count')
    return render(request, "home.html",
            {"videos": videos})


def upload(request):
    "upload page"
    if True:
        redirect("home")
    return render(request, "upload.html")


def view(request, video_id):
    "view video"
    video = get_object_or_404(Video, id=video_id)
    video.increment_view()
    return render(request, "view.html",
            {"video": video})
