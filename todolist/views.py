
from django.shortcuts import render

def todolist(request):
    return render(request, 'todolist/index.html',)
