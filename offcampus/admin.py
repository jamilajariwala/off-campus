from django.contrib import admin
from .models import *
from django.utils.html import format_html
#class ImageAdmin(admin.ModelAdmin):
   # def image_tag(self,obj):
      #  return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.m_livingroom.url))
    #list_display=['username','useremail','userphone','userfeedback']

admin.site.register(Flat_Images)

class Flat_imagesinline(admin.TabularInline):
    model=Flat_Images

@admin.register(Flats)
class Faltinline(admin.ModelAdmin):
    inlines=[Flat_imagesinline]
    
admin.site.register(Aminities)
admin.site.register(My_booking)
admin.site.register(city)
admin.site.register(Feedback)
admin.site.register(userregister)
# Register your models here