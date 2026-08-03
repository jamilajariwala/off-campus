"""
URL configuration for pg_finding_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from offcampus import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('view_flat/<int:id>',views.view_flat,name='view_flat'),
    path('view_property/',views.viewproperty,name='viewproperty'),
    path('fd/',views.feedback,name='feedback'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.userlogout,name='logout'),
    path('booking/',views.Booking,name='booking'),
    path('rules/',views.rules,name='rules'),
     path('view_book/',views.view_booking,name='view_booking'),
     path('cityroom/<int:id>',views.cityroom,name="cityroom"),
     path('login/',views.userlogin,name='userlogin')
]
