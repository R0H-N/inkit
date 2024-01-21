from django.db.models import Q 
from .models import project as projectmodel
from .models import Tag



def searchProjects(request):
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains= search_query)

    project = projectmodel.objects.distinct().filter(
        Q(title__icontains = search_query) |
        Q(description__icontains = search_query) |
        Q(owner__name__icontains = search_query) |
        Q(tags__in = tags)

    )
    return project,search_query
