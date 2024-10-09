from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'third_task/home.html')

def page1(request):
    return render(request, 'third_task/page1.html')

def page2(request):
    return render(request, 'third_task/page2.html')