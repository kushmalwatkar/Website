from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def projects(request):
    return render(request, "projects.html")

def project(request, project_name):
    return render(request, "project.html", {"project_name": project_name})

def experience(request):
    return render(request, "experience.html")

def contact(request):
    return render(request, "contact.html")