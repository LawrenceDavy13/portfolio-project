from django.shortcuts import render

def mathswebsite(request):
    return render(request, 'mathswebsite/index.html')
