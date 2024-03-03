from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerializer
from project.models import project,review,Tag

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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectReview(request,pk):
    projects = project.objects.get(id=pk)
    user = request.user.profile
    data = request.data

    Review,create = review.objects.get_or_create(
        owner=user,
        project = projects,
    )
    Review.value = data['value']
    Review.save()
    project.getVoteCount


    serializer = ProjectSerializer(projects,many=False)
    return Response(serializer.data)