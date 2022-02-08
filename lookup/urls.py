from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name ="home"),
   path('about.pepasyawapalaseca', views.about, name ="about"),		#  the thing with this is that it calls the views and then it
   # calls the about part 


]
