from django.shortcuts import render
from .models import Menu, Config, Imageslider
from typing import Dict

def merge_config(params:Dict):
    configs = Config.objects.all()
    
    map_configs = {}
    for config in configs:
        map_configs[config.code] = config.content
    params["map_configs"] = map_configs
    # print("map config",params["map_configs"]) # comment dong nay thi dc, vì param co may item khoong print ra dc
    return params

def my_render(request, template, params):
    return render(request,template,merge_config(params))


def index(request):
    menu=Menu.objects.all()[:8]
    menu2=Menu.objects.all()[8:]
    imageslider=Imageslider.objects.all()

    contex={"menu":menu,"menu2":menu2,"imageslider":imageslider}
    return my_render(request,"coffee/index.html", contex)

# Create your views here.
