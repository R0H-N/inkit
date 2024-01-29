from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer
from project.models import project

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET':'/api/project'},
        {'GET':'/api/project/id'},
        {'POST':'/api/project/id/vote'},

        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},
        
    ]
    return Response(routes)

@api_view(['GET'])
def getProjects(request):
    projects = project.objects.all()
    serializer = ProjectSerializer(projects,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request,pk):
    proj = project.objects.get(id=pk)
    serializer = ProjectSerializer(proj,many=False)
    return Response(serializer.data)