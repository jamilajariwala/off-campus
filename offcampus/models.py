from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User

# Create your models here.\

class Aminities(models.Model):
    name=models.CharField(max_length=100)
    logo=models.ImageField( upload_to='static/images/asset/logo')

    def __str__(self):
        return self.name
    
GENDER_CHOICE=(('Male','male'),
               ('Female','feamle'),
               ('Co-living','co-living'))
class city(models.Model):
    city=models.CharField(max_length=100) 
    cityimg=models.ImageField(upload_to="static/images/asset")

    def __str__(self):
        return self.city

class Flats(models.Model):
    
    flat_name=models.CharField(max_length=100)
    city=models.ForeignKey(city,on_delete=models.CASCADE)
    bhk=models.CharField(max_length=200)
    address=models.TextField()
    livingroom=models.ImageField(upload_to="static/images/asset/rooms/flats",default=None)
    gender=models.CharField(max_length=100,choices=GENDER_CHOICE,default=None)
    aminitie=models.ManyToManyField(Aminities)
    details=models.TextField()
    
    def __str__(self):
        return self.flat_name +" "+ str(self.city)

class Flat_Images(models.Model):
    flat_name=models.ForeignKey(Flats,on_delete=models.CASCADE,null=True)
    image=models.ImageField(upload_to="static/images/asset/rooms/flats",blank=True)
    nearby=models.CharField(max_length=200,blank=True)
    km=models.CharField(max_length=100,default=None,blank=True)
    accommodation=models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.flat_name.flat_name

class Feedback(models.Model):
    username=models.CharField(max_length=100)   
    useremail=models.EmailField() 
    userphone=models.CharField(max_length=10)  
    satisfy=models.CharField(max_length=10) 
    feedback=models.TextField()

    def __str__(self):
        return self.username +" "+ self.useremail +" "+ self.userphone  +" "+ self.feedback
class userregister(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)

class My_booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100) 
    last_name=models.CharField(max_length=100) 
    student_cno=models.CharField(max_length=100) 
    parent_cno=models.CharField(max_length=100) 
    student_email=models.EmailField() 
    parent_email=models.EmailField()
    gender=models.CharField(max_length=100) 
    address=models.TextField()
    check_in_date=models.CharField(max_length=100)
    check_out_date=models.CharField(max_length=100)
    type=models.CharField(max_length=100) 
    payment_mode=models.CharField(max_length=100) 

    def __str__(self):
        return self.first_name +" "+ self.last_name