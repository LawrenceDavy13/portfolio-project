
from django.shortcuts import render

def mathsgame(request):
    return render(request, 'mathsgame/index.html',)
