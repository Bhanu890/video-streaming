from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Video
from django.conf import settings

# Create your views here    .
def home(request):
    videos = Video.objects.order_by('-created_at')

    return render(request,
                  'videos/home.html',
                  {'videos': videos},
    )
    #return render(request, 'videos/home.html')
    #return HttpResponse("Hello, welcome to the video streaming app!")

def watch_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)

    return render(request, 
                    "videos/watch.html", 
                    {
                        "video":video,
                        "MEDIA_URL": settings.MEDIA_URL
                    },
    )

    
