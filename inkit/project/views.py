from django.shortcuts import render

from django.http import HttpResponse


def project(request):
    page = 'project'
    number = 9
    context={ 'page':page, 'number':number}
    
    return render(request,'project/project.html', context )

def proj(request, pk):
    return render(request,'project/proj.html')

def createProject(request):
    context = {
    }
    return render(request ,"project/project_form.html",context)