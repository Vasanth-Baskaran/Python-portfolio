from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project

# Create your views here.
def project_list(request):
    return render(request, 'projects/index.html')

def all_project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html', {'projects':projects})

def detail_view(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/details.html', {'project':project})