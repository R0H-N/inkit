from django.shortcuts import render

from django.http import HttpResponse
from .models import project as projectmodel
from .forms import projectForm


def project(request):
    project = projectmodel.objects.all()
    context={ 'project': project }
    
    return render(request,'project/project.html', context )

def proj(request, pk):
    projectObj = projectmodel.objects.get(id = pk )

    return render(request,'project/proj.html',{'project':projectObj})

def createProject(request):
    form = projectForm()

    context = {'form':form 
    }
    return render(request ,"project/project_form.html",context)