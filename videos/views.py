from django.shortcuts import render
from django.http import HttpResponse
from .models import Video

# Create your views here    .
def home(request):
    videos = Video.objects.order_by('-created_at')

    return render(request,
                  'videos/home.html',
                  {'videos': videos},
    )
    #return render(request, 'videos/home.html')
    ##return HttpResponse("Hello, welcome to the video streaming app!")
