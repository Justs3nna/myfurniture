from django.shortcuts import render

def home(request):
 return render(request, 'homepage.html')

def aboutus(request):
 return render(request, 'aboutus.html')
