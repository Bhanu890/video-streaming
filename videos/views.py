from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'videos/home.html')
##return HttpResponse("Hello, welcome to the video streaming app!")