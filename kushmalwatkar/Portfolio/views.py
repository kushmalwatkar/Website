from django.shortcuts import render
from django.http import HttpResponse

from django.conf import settings

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def projects(request):
    return render(request, "projects.html", {"projects": settings.PORTFOLIO_PROJECTS})

def project(request, project_name):
    for project in settings.PORTFOLIO_PROJECTS:
        if project["web-name"] == project_name:
            return render(request, "project.html", {"project": project})
    return render(request, "projects.html")

def experience(request):
    return render(request, "experience.html")

def contact(request):
    return render(request, "contact.html")