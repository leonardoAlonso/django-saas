from django.shortcuts import render

from visits.models import PageVisit


def home(request, *args, **kwargs):
    return about(request, *args, **kwargs)

def about(request, *args, **kwargs):
    
    qs = PageVisit.objects.all()
    path_qs = PageVisit.objects.filter(path=request.path)
    context_dict = {
        'page_title': 'hello world',
        'page_visits': qs.count(),
        'path_visits': path_qs.count(),
        'percent': path_qs.count() / qs.count() * 100,
    }
    
    PageVisit.objects.create( path=request.path )

    return render(request, 'home.html', context_dict)

