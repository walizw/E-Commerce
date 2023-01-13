from django.shortcuts import render

def store (request):
    return render (request, "store/index.html")