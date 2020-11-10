from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
     return render(request, 'Home.html')

def about(request):
    return render(request, "about.html")
def count(request):
    fulltext = request.GET['userinput']
    wordlist = fulltext.split()
    number = len(wordlist)
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1
    
    sortedthings = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse = True)
    return render(request, 'Count.html',{'fulltext':fulltext, 'countit':number, 'worddic' : sortedthings})