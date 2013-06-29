# Create your views here.
from django.http import HttpResponse
from django.template import Context#, loader
from django.shortcuts import render#, get_object_or_404
from models import Waypoint
from models import WorldBorder
#from django.http import Http404


#===============================================================================
# def outputPersonInfo(request):
#    person = get_object_or_404(Person, id=0)
#    output = "aaa" 
#    if(person):
#        output = "bbb" + person.id
#    return HttpResponse(output)
#===============================================================================

def outputMapInfo(request):
    state = ""
    user = request.user
    if user.is_authenticated():
        state = 'Welcome ' + user.username
    else:
        state = "please login"
    'Display map'
    waypoints = Waypoint.objects.order_by('name')
    context = Context({
         'waypoints': waypoints,
         'state': state,
     })
    #print(waypoints)
    return render(request, 'mapview.html', context)
#     try:
#         person = Person.objects.using('default').get(id=1)
#     except Person.DoesNotExist:
#         return HttpResponse("no person exist!!")
#         #raise Http404      
#     context = Context({
#         'person': 1,
#     })
#     #return HttpResponse(template.render(context))
#     return render(request, 'mapview.html', context)
    
def showLocation(request):
    'showlocation map'
    waypoints = Waypoint.objects.order_by('name')  
    worldborder = WorldBorder.objects.get(name="China")
    geo = 'POINT('+str(worldborder.lon)+' '+str(worldborder.lat)+')'
    waypoint = Waypoint(name=worldborder.name, geometry=geo)
    context = Context({
         'waypoint': waypoint,#waypoints[0],
     })
    #print(waypoints)
    return render(request, 'showlocation.html', context)
    