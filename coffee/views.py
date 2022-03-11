from django.shortcuts import render
from .models import Menu, Config

def index(request):
    menu=Menu.objects.all()[:2]
#     qs = MyModel.objects.filter(blah = blah)
# if qs.count() > 0:
#     return qs[0]
# else:
#     return None
    contex={"menu":menu}
    return render(request,"coffee/index.html", contex)

# Create your views here.
