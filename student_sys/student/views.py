from django.shortcuts import render

def index(request):
    words = "World"
    return render(request, 'index.html', context={"words":words})
