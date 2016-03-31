from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
# Create your views here.

def show_cont(request):
    respuesta="<ul>"
    list_cont=Pages.objects.all()
    for cont in list_cont :
        respuesta+="<li>"+cont.name+" "+cont.page+"</li>"
    respuesta+="</ul>"
    return HttpResponse(respuesta)

def save_cont(request,name,cont):
    obj=Pages(name=name,page=cont)
    obj.save()
    return HttpResponse("<h1> Guardado.."+name+"</h1>")

def get_cont(request,name):
    try:
        obj=Pages.objects.get(name=name)
        return HttpResponse(obj.page)
    except Pages.DoesNotExist:
        return HttpResponse(" 404 Not Found")
def error(request,cont1,cont2):
    return HttpResponse("404 Not Found")
