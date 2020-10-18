from django.urls import path
from myhomechef import views

urlpatterns = [
    
    path("", views.frontpage , name="frontpage")
    
]
 