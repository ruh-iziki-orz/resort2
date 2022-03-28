from distutils.command.upload import upload
import email
from email import message
from re import VERBOSE
from sre_parse import Verbose
from tabnanny import verbose
from django.db import models
#from phone_field import PhoneField
# Create your models here.
class Regions(models.Model):
    name=models.CharField(verbose_name="region name", max_length=50)
    def __str__(self):
        return str(self.name)
class Areas(models.Model):
    name=models.CharField(verbose_name="area name", max_length=50)
    region=models.ForeignKey(Regions,verbose_name="of region",on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.name)+"  in "+str(self.region)

class Airports(models.Model):
    name=models.CharField(verbose_name="name of airport ", max_length=50)
    area=models.ForeignKey(Areas,verbose_name="in area",on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)
    
class Travel_Classes(models.Model):
    name=models.CharField(verbose_name="travel class",max_length=50)
    def __str__(self):
        return str(self.name)
class Titles(models.Model):
    name=models.CharField(verbose_name="Title",max_length=50)
    def __str__(self):
        return str(self.name)

    

class Room_Type(models.Choices):
    person="one"
    couple="couple"
    family="family"
class Features(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return str(self.name)

class Hotel_Types(models.Model):
    name=models.CharField(max_length=30,null=True)
    def __str__(self):
        return str(self.name)
class Points(models.Model):
    main=models.BooleanField(default=False)
    name=models.CharField(max_length=30)
    desc=models.TextField(null=True,blank=True)
    sub=models.TextField(null=True,blank=True)
    def __str__(self):
        return str(self.name)


class Accomidations(models.Model):
    self_id=models.CharField(max_length=50,unique=True,auto_created=True)
    name=models.CharField(max_length=50,blank=True,null=True)
    summary=models.TextField(null=True)
    def __str__(self):
        return str(self.self_id)
    
class Accomidations_Sub(models.Model):
    accomidation=models.ForeignKey(Accomidations,verbose_name="Accomidation", on_delete=models.CASCADE)
    self_id=models.CharField(verbose_name="unique rooms", max_length=50,unique=True,auto_created=True)
    image=models.ImageField(upload_to="assests/rooms",null=True,blank=True)
    name=models.CharField(verbose_name="Room name",max_length=50)
    rooms=models.IntegerField(verbose_name="no of rooms",blank=True,null=True)
    room_view=models.CharField(max_length=50,blank=True,null=True)
    facilities=models.TextField(blank=True,null=True)
    def __str__(self):
        return str(self.self_id)

class Dining(models.Model):
    self_id=models.CharField(verbose_name="name to this dining",max_length=50,unique=True,auto_created=True)
    name=models.CharField(verbose_name="Dining Name",max_length=50)
    summary=models.TextField(blank=True)
    def __str__(self):
        return str(self.self_id)
    
class Dining_Sub(models.Model):
    dining=models.ForeignKey(Dining,on_delete=models.CASCADE)
    self_id=models.CharField(max_length=50,unique=True,auto_created=True)
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="rooms",null=True,blank=True)
    cuisine=models.TextField(blank=True)
    setting=models.TextField(blank=True)
    dress_code=models.TextField(blank=True)
    childrens=models.TextField(blank=True)
    vegetarian=models.TextField(blank=True)
    reservation=models.TextField(blank=True)
    def __str__(self) -> str:
        return str(self.self_id)+str(self.dining)

class Property(models.Model):
    self_id=models.CharField(verbose_name="name to this property",max_length=50,unique=True,auto_created=True)
    name=models.CharField(verbose_name="Property HighLights Name",max_length=50)
    def __str__(self):
        return str(self.self_id)

class Property_Sub(models.Model):
    property=models.ForeignKey(Property,on_delete=models.CASCADE)
    self_id=models.CharField(verbose_name="name to this property_sub",max_length=50,unique=True,auto_created=True)
    name=models.CharField(verbose_name="Property sub Name",max_length=50)
    summary=models.TextField(blank=True)
    image=models.ImageField(upload_to="property",blank=True)
    def __str__(self):
        return str(self.self_id)


class Hotel_Infos(models.Model):
    title=models.CharField(max_length=30)
    self_id=models.CharField(max_length=50,verbose_name=" name  unique to specific hotel",unique=True,auto_created=True)
    area=models.ForeignKey(Areas,on_delete=models.CASCADE)
    price_dec=models.CharField(max_length=100,null=True,blank=True)
    overview=models.TextField(null=True,blank=True)
    features=models.ManyToManyField(Features,blank=True)
    location=models.TextField(verbose_name="Location",null=True,blank=True)
    accomidation=models.ForeignKey(Accomidations,on_delete=models.SET_NULL,null=True)
    dining=models.ForeignKey(Dining,on_delete=models.CASCADE)
    property=models.ForeignKey(Property,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return str(self.self_id)



class Offers(models.Model):
    hotel_type=models.ForeignKey(Hotel_Types,on_delete=models.CASCADE,null=True)
    hotel=models.ForeignKey(Hotel_Infos,on_delete=models.CASCADE)
    main_screen=models.BooleanField(default=False)
    self_id=models.CharField(max_length=50,verbose_name="name specific to offer",unique=True,auto_created=True)
    name=models.CharField(verbose_name="offer name",max_length=50)
    summary=models.TextField(blank=True)
    feature=models.TextField(blank=True)
    rooms=models.TextField(blank=True)
    airport=models.ForeignKey(Airports, on_delete=models.CASCADE)
    validity=models.TextField(blank=True)
    image=models.ImageField(upload_to="offer_image/")
    from_price=models.IntegerField(null=True,blank=True)
    comment=models.TextField(null=True,blank=True)
    #from_room_type=models.CharField(max_length=15,choices=Room_Type.choices,null=True,blank=True)
    #saving_prince=models.IntegerField(null=True,blank=True)
    #saving_room_type=models.CharField(max_length=15,choices=Room_Type.choices,null=True,blank=True)
    points=models.ManyToManyField(Points)
    def __str__(self):
        return str(self.self_id)

class Situationsal_Pricing(models.Model):
    situation=models.CharField(max_length=20)
    price=models.IntegerField()
    per=models.CharField(max_length=10,choices=Room_Type.choices)
    offer=models.ForeignKey(Offers,parent_link=True,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.situation)+str(self.per)
class travels(models.Model):
    self_id=models.CharField(max_length=50,unique=True,auto_created=True)
    quote=models.CharField(max_length=50,null=True)
    date=models.DateField(null=True)
    name=models.CharField(max_length=50,null=True,blank=True)
    auther=models.CharField(max_length=50,blank=True)
    cover=models.ImageField(upload_to="travels")
    image=models.ImageField(upload_to="travels")
    summary=models.TextField(blank=True)
    sub_summary=models.TextField(blank=True)
    def __str__(self):
        return str(self.self_id)
class Min_Pricing(models.Model):
    amount=models.IntegerField()
    def __str__(self) -> str:
        return str(self.amount)

class Photos(models.Model):
    image=models.ImageField(upload_to="hotels/")
    hotel_info=models.ForeignKey(Hotel_Infos,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.hotel_info)

class Quote(models.Model):
    title=models.CharField(max_length=30,verbose_name='Title',null=True)
    name=models.CharField(max_length=50,null=True)
    #first_name=models.CharField(verbose_name="First Name",max_length=50)
    #last_name=models.CharField(verbose_name="last name",max_length=50)
    email_id=models.EmailField(verbose_name="E-mail", max_length=254)
    phone_no=models.CharField(verbose_name="phone_no",max_length=15,null=True)
    time=models.TimeField(auto_created=True,null=True)
    adults=models.IntegerField(verbose_name="Adults")
    children=models.IntegerField(verbose_name="children")
    #date_of_travel=models.DateField(verbose_name="Date of Travel")
    fromDate=models.DateField(verbose_name="from Date",null=True)
    toDate=models.DateField(verbose_name="to Date",null=True)
    duration=models.IntegerField(verbose_name="Duration")
    budget=models.CharField(verbose_name="budget",null=True,max_length=50)
    departure=models.ForeignKey(Airports, verbose_name=("Departure Airport"), on_delete=models.SET_NULL,null=True)
    travel_class=models.ForeignKey(Travel_Classes,verbose_name="Travel Class",on_delete=models.SET_NULL,null=True)
    comment=models.TextField(verbose_name="Comments")
    offer=models.ForeignKey(Offers,verbose_name="offer",on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return str(self.name) +" "+str(self.offer)

class Budgets(models.Model):
    name=models.CharField(null=True,max_length=50)
    def __str__(self) -> str:
        return self.name
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    time=models.TimeField(auto_created=True,null=True)
    subject=models.TextField(blank=True,null=True)
    message=models.TextField(blank=True,)
    def __str__(self):
        return str(self.email)+str(self.time)
    