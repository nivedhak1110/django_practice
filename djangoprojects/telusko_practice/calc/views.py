from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'nivedha'})

# method to add two numbers
def add(request):
    print(request)
    num1 = int(request.POST['num1'])
    print(num1)
    num2 = int(request.POST['num2'])
    print(num2)
    sum = num1 + num2
    return render(request,'home.html',{'sum': sum })