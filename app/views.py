from django.shortcuts import render

# Create your views here.

from app.models import *

def display_topic(request):
    LOT=Topic.objects.all()

    LOT=Topic.objects.all()

    d={'topic':LOT}

    return render(request,'display_topic.html',d)

def display_webpage(request):
    LOW=Webpag.objects.all()
    
   
    d={'webpage':LOW}
    return render(request,'display_webpage.html',d)


def display_accessrecords(request):
    LOA=Accessrecord.objects.all()
    d={'access':LOA}
    return render(request,'display_accessrecords.html',context=d)