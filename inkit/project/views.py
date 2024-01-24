from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q  

from django.http import HttpResponse
from .models import project as projectmodel
from .models import Tag
from .forms import projectForm,ReviewForm
from .utils import searchProjects,paginateProjects
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def project(request):
    search_query = ''
    project,searchProject = searchProjects(request)
    
    custom_range,project = paginateProjects(request,project,3)

    context={ 'project': project , 'search_query':search_query , 'custom_range':custom_range}
    
    return render(request,'project/project.html', context )

def proj(request, pk):
    projectObj = projectmodel.objects.get(id = pk )
    form = ReviewForm()
    context = { 'project':projectObj,'form':form}

    return render(request,'project/proj.html',context)

@login_required(login_url='login')
def createProject(request):
    form = projectForm()

    if request.method == 'POST':
        form = projectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project')
    context = {'form':form 
    }
    return render(request ,"project/project_form.html",context)

@login_required(login_url='login')
def updateProject(request,pk):
    project = projectmodel.objects.get(id=pk)
    form = projectForm(instance=project)

    if request.method == 'POST':
        form = projectForm(request.POST ,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('project')
    context = {'form':form 
    }
    return render(request ,"project/project_form.html",context)

@login_required(login_url='login')
def deleteProject(request,pk):
    project = projectmodel.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project')
    context = {'object':project}
    return render(request,"project/delete_template.html",context)
