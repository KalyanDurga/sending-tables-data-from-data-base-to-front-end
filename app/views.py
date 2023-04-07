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
    
    #LOW=Webpag.objects.filter(topic_name='cricket')
    #LOW=LOW=Webpag.objects.order_by('topic_name')   #--> for assending order

    #LOW=LOW=Webpag.objects.order_by('-topic_name')   #--> for Desending order

    #LOW=LOW=Webpag.objects.exclude(topic_name='football')   #--> for excluding that pirtucular record and printing all

    from django.db.models.functions import Length

    LOW=LOW=Webpag.objects.order_by(Length('topic_name'))   #--> for aranging by its length  in assending order 

    LOW=LOW=Webpag.objects.order_by(Length('topic_name').desc())   #--> for aranging by its length  in desending order




    d={'webpage':LOW}
    return render(request,'display_webpage.html',d)


def display_accessrecords(request):
    LOA=Accessrecord.objects.all()

    LOA=Accessrecord.objects.filter(date__gt='2001-12-31')  #--> gt for greater than

    LOA=Accessrecord.objects.filter(date__lt='2001-12-31')

    LOA=Accessrecord.objects.filter(date__gte='1998-12-31')

    LOA=Accessrecord.objects.filter(date__lte='2001-12-31')

    d={'access':LOA}
    return render(request,'display_accessrecords.html',context=d)