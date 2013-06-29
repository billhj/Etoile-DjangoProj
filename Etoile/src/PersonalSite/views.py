# Create your views here.
from django.http import HttpResponse
from django.template import Context#, loader
from django.shortcuts import render#, get_object_or_404
#from django.http import Http404
from models import Person

def index(request):
    return HttpResponse("Hello, world. You're at the PersonInfo.")


#===============================================================================
# def outputPersonInfo(request):
#    person = get_object_or_404(Person, id=0)
#    output = "aaa" 
#    if(person):
#        output = "bbb" + person.id
#    return HttpResponse(output)
#===============================================================================

def outputPersonInfo(request):
    try:
        person = Person.objects.using('default').get(id=1)
    except Person.DoesNotExist:
        return HttpResponse("no person exist!!")
        #raise Http404      
    context = Context({
        'person': person,
    })
    #return HttpResponse(template.render(context))
    return render(request, 'personalinfo.html', context)


