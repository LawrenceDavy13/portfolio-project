from django.http import HttpResponse
from django.shortcuts import render
import operator
# from .models import wordcounter

def piglatintranslator(request):
    return render(request, 'piglatintranslator/piglatintranslator.html')

def translate(req):
    original = req.GET['originaltext'].lower()

    translation = ''
    for word in original.split():
        if word[0] in ['a', 'e', 'i', 'o', 'u']:
            translation += word
            translation += 'yay '
        else:
            translation += word[1:]
            translation += word[0]
            translation += 'ay '          


    return render(req, 'piglatintranslator/translate.html', {'original': original, 'translation': translation})    


