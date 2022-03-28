from multiprocessing import context
from django.shortcuts import render
from numpy import minimum
from .models import *
from django.http import JsonResponse
from django.db.models import Q
# Create your views here.
def index(request):
    regions=Regions.objects.all
    types=Hotel_Types.objects.all
    header=Offers.objects.filter(main_screen=True)
    offers=Offers.objects.filter(main_screen=False)
    minimum=Min_Pricing.objects.all
    
    travel=travels.objects.all
    areas=Areas.objects.all
    print(offers)
    return render(request,'index.html',{"header":header,"offers":offers,"travels":travel,"areas":areas,"regions":regions,"types":types,"minimum":minimum})
def resort(request):
    #print(args,kwargs)
    print(request.GET['offer'])
    offer_id=request.GET['offer']
    offers=Offers.objects.get(id=offer_id)
    hotel_id =list(Offers.objects.filter(id=offer_id).values_list('hotel_id',flat=True))[0]
    hotel=Hotel_Infos.objects.get(id=hotel_id)
    accomidation_id=Hotel_Infos.objects.filter(id=hotel_id).values_list("accomidation_id",flat=True)
    accomidation_sub=Accomidations_Sub.objects.filter(accomidation_id__in=accomidation_id)
    dining_id=Hotel_Infos.objects.filter(id=hotel_id).values_list("dining_id",flat=True)
    dining_sub=Dining_Sub.objects.filter(dining_id__in=dining_id)
    property_id=Hotel_Infos.objects.filter(id=hotel_id).values_list("property_id",flat=True)
    property_sub=Property_Sub.objects.filter(property_id__in=property_id)
    minimum=Min_Pricing.objects.all()
    photo=Photos.objects.filter(hotel_info_id=hotel_id)
    regions=Regions.objects.all()
    types=Hotel_Types.objects.all()
    areas=Areas.objects.all()
    situationsal_price=Situationsal_Pricing.objects.filter(offer_id=offer_id)
    return render(request,'resorts-single.html',{"hotel":hotel,"photos":photo,"offer":offers,"situational_price":situationsal_price,"accomidation_sub":accomidation_sub,'dining_sub':dining_sub,"areas":areas,"property_sub":property_sub,"regions":regions,"types":types,"minimum":minimum})
def about(request):
    minimum=Min_Pricing.objects.all()
    regions=Regions.objects.all()
    types=Hotel_Types.objects.all()
    areas=Areas.objects.all()
    return render(request,'about.html',{"areas":areas,"regions":regions,"types":types,"minimum":minimum})
def grid(request):
    regions=Regions.objects.all
    types=Hotel_Types.objects.all
    minimum=Min_Pricing.objects.all
    areas=Areas.objects.all
    offers=Offers.objects.all
    return render(request,'resorts-grid.html',{"offers":offers,"regions":regions,"types":types,"minimum":minimum,"areas":areas})
def travel_grid(request):
    regions=Regions.objects.all
    types=Hotel_Types.objects.all
    minimum=Min_Pricing.objects.all
    areas=Areas.objects.all
    travel=travels.objects.all
    return render(request,'travel-grid.html',{"travels":travel,"regions":regions,"types":types,"minimum":minimum,'areas':areas})
def travel_single(request):
    id=int(request.GET["travel"])
    travel=travels.objects.get(id=id)
    regions=Regions.objects.all
    types=Hotel_Types.objects.all
    minimum=Min_Pricing.objects.all
    areas=Areas.objects.all
    return render(request,'travel-single.html',{"travel":travel,"regions":regions,"types":types,"minimum":minimum,'areas':areas})
def contact(request):
    regions=Regions.objects.all
    types=Hotel_Types.objects.all
    minimum=Min_Pricing.objects.all
    areas=Areas.objects.all
    return render(request,"contact.html",{"regions":regions,"types":types,"minimum":minimum,'areas':areas})
def search(request):
    print(request.method)
    keyword=request.GET['keyword']
    type=int(request.GET["type"])
    regions=int(request.GET["region"])
    areas=int(request.GET["area"])
    minimum=int(request.GET['min'])
    #pg_no=int(request.GET['pg_no'])
    print(keyword,type,regions,minimum,areas)
    hotel_ids=Hotel_Infos.objects.all().values_list("id", flat=True)
    if type!=-1:
        hotel_ids=Hotel_Infos.objects.filter(type_id=type).values_list("id",flat=True)
    print(hotel_ids)
    if areas==-1:
        if regions!=-1:
            areas=Areas.objects.filter(region_id=regions).values_list("id",flat=True)
            hotel_ids=Hotel_Infos.objects.filter( area_id__in=areas,id__in=hotel_ids).values_list("id",flat=True)
    else:
        areas=Areas.objects.filter(id=areas).values_list("id",flat=True)
        hotel_ids=Hotel_Infos.objects.filter( area_id__in=areas,id__in=hotel_ids).values_list("id",flat=True)
    print(areas)
    if len(keyword)>0:
        qs=Q(title__icontains=keyword)
        hotel_ids=Hotel_Infos.objects.filter(qs,id__in=hotel_ids).values_list("id",flat=True)
    if minimum==-1:
        offers=Offers.objects.filter( hotel__id__in=hotel_ids)
    else:
        offers=Offers.objects.filter(from_price__lte=minimum, hotel_id__in=hotel_ids)
    regions=Regions.objects.all
    types=Hotel_Types.objects.all
    minimum=Min_Pricing.objects.all
    areas=Areas.objects.all
    return render(request,'resorts-grid.html',{"offers":offers,"regions":regions,"areas":areas,"types":types,"minimum":minimum})

def quote(request):
    print(request)
    context={}
    offer_id=request.POST['offer']
    offers=Offers.objects.get(id=offer_id)
    regions=Regions.objects.all
    types=Hotel_Types.objects.all
    minimum=Min_Pricing.objects.all
    areas=Areas.objects.all
    titles=Titles.objects.all
    airports=Airports.objects.all
    travelClass=Travel_Classes.objects.all
    context={"message":"something went wrong "}
    if request.method=='POST':
        offer=Offers.objects.get(id=int(request.POST['offer']))
        title=request.POST['title']
        name=request.POST['name']
        email=request.POST['email']
        phone_no=request.POST['tel']
        adults=int(request.POST['adults'])
        children=int(request.POST['children'])
        fromDate=request.POST['fromDate']
        toDate=request.POST['toDate']
        duration=request.POST['duration']
        airport=Airports.objects.get(id=int(request.POST['airport']))
        travel_class=Travel_Classes.objects.get(id=int(request.POST['travelclass']))
        comment=request.POST['comment']
        budget=request.POST['budget']
        children=int(request.POST['children'])
        budgets=Budgets.objects.all
        print(name,email,phone_no,offer,comment)
        quote=Quote(title=title,name=name,email_id=email,phone_no=phone_no,adults=adults,children=children,fromDate=fromDate,toDate=toDate,duration=duration,travel_class=travel_class,comment=comment,offer=offer,departure=airport,budget=budget)
        quote.save()
        message=True
        context={
                "message":"Your submissions has been received we will contact you soon "
                }
    return render(request,"request-quote.html",{"context":context,"travelClass":travelClass,"airports":airports,"titles":titles,"offer":offers,"regions":regions,"types":types,"minimum":minimum,'areas':areas,"budgets":budgets})
    # return render(request, "contact.html", context=context)
    #return render(request,"contact.html",context=context)
def areas_list(request,*args, **kwargs):
    region_id=int(kwargs.get('selected'))
    print(region_id)
    if region_id==-1:
        areas=list(Areas.objects.all().values())
        return JsonResponse({"areas":areas})
    areas=list(Areas.objects.filter(region_id=region_id).values())
    print(areas)
    return JsonResponse({"areas":areas})
    areas_list=area.objects.filter()
def request_quote(request):
    offer_id=request.GET['offer']
    offers=Offers.objects.get(id=offer_id)
    regions=Regions.objects.all
    types=Hotel_Types.objects.all
    minimum=Min_Pricing.objects.all
    areas=Areas.objects.all
    titles=Titles.objects.all
    airports=Airports.objects.all
    travelClass=Travel_Classes.objects.all
    budgets=Budgets.objects.all
    context={"message":""}
    return render(request,"request-quote.html",{"context":context,"travelClass":travelClass,"airports":airports,"titles":titles,"offer":offers,"regions":regions,"types":types,"minimum":minimum,'areas':areas,"budgets":budgets})


def contact_form(request):
    print(request.POST)
    context={"message":"something went wrong"}
    regions=Regions.objects.all
    types=Hotel_Types.objects.all
    minimum=Min_Pricing.objects.all
    areas=Areas.objects.all
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        con_form=Contact(name=name,email=email,subject=subject,message=message)
        con_form.save()
        context={"message":"we will get back to you soon"}
       
    return render(request,"contact.html",{"context":context,"regions":regions,"types":types,"minimum":minimum,'areas':areas})

