from django.shortcuts import render

def class_based_view(request):
    return render(request, 'second_task/class_based.html')

def function_based_view(request):
    return render(request, 'second_task/function_based.html')