from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def today(request):
    return render(request, 'today.html')

def django(request):
    return render(request, 'django.html')