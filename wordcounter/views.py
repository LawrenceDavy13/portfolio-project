from django.http import HttpResponse
from django.shortcuts import render
import operator
# from .models import wordcounter

def wordcounter(request):
    return render(request, 'wordcounter/wordcounter.html')

def count(request):

    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            # Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'wordcounter/count.html', {'fulltext': fulltext, 
                            'count': len(wordlist), 
                            'sortedwords': sortedwords})


