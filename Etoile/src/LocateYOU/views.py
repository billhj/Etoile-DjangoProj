from django.http import HttpResponse
from django.template import Context#, loader
from django.shortcuts import render#, get_object_or_404
from models import Waypoint
from models import WorldBorder
#from django.http import Http404


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
    
def showLocation(request):
    waypoints = Waypoint.objects.order_by('name')  
    worldborder = WorldBorder.objects.get(name="China")
    geo = 'POINT('+str(worldborder.lon)+' '+str(worldborder.lat)+')'
    waypoint = Waypoint(name=worldborder.name, geometry=geo)
    context = Context({
         'waypoint': waypoint,#waypoints[0],
         'user': request.user,
         'path': request.path,
     })
    #print(waypoints)
    return render(request, 'showlocation.html', context)

def locateU(request):
    worldborder = WorldBorder.objects.get(name="China")
    geo = 'POINT('+str(worldborder.lon)+' '+str(worldborder.lat)+')'
    waypoint = Waypoint(name=worldborder.name, geometry=geo)
    context = Context({
         'waypoint': waypoint,#waypoints[0],
         'user': request.user,
         'path': request.path,
     })
    #print(waypoints)
    return render(request, 'locateU.html', context)
    