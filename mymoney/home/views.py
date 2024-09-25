from django.shortcuts import render

def homepage():
    return render(request, 'main/index.html')
