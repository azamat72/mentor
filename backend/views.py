from django.shortcuts import redirect, render
from .models import Agent, Post, Lead


def index(request):
    data = Post.objects.all()
    return render(request, "index.html", {'post': data})

def about(request):
    data = Post.objects.all()
    return render(request, "about.html", {'post': data})

def news(request):
    data = Lead.objects.all()
    return render(request, "news.html", {'lead': data})

def events(request):
    data = Post.objects.all()
    return render(request, "events.html", {'post': data})

def agents(request):
    data = Agent.objects.all()
    return render(request, "agents.html", {'agent': data})

def contact(request):
    data = Post.objects.all()
    return render(request, "contact.html", {'post': data})


