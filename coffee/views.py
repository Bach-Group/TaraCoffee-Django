from django.shortcuts import render
from .models import Menu, Config

def index(request):
    menu=Menu.objects.all()[:8]
    menu2=Menu.objects.all()[8:]
#     qs = MyModel.objects.filter(blah = blah)
# if qs.count() > 0:
#     return qs[0]
# else:
#     return None
    contex={"menu":menu,"menu2":menu2}
    return render(request,"coffee/index.html", contex)

# Create your views here.
