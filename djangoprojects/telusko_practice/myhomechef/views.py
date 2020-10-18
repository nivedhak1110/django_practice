from django.shortcuts import render
from .models import Recipies,Food

# Create your views here.

# home page render
def frontpage(request):
    print(request)
    Food_items = Food.objects.all()
    return render(request,"frontpage.html", {'Food_items':Food_items })




