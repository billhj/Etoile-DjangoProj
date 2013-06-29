# Create your views here.
from django.http import HttpResponse
from django.template import Context#, loader
from django.shortcuts import render
from models import Publication

def index(request):
    return HttpResponse("Hello, world. You're at the Publication index.")


def outputPublications(request):
    publication_list = Publication.objects.using('default').order_by('year')
    #template = loader.get_template('publications.html')
    context = Context({
        'publication_list': publication_list,
    })
    #return HttpResponse(template.render(context))
    return render(request, 'publications.html', context)