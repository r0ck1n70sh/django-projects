from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost

def archive(request):
    posts= BlogPost.objects.order_by('-timestamp')
    context= {'posts': posts}
    return render(request, 'archive.html', context)

