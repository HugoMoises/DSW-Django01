from django.shortcuts import render

def index(request):
    return render(request, "estudio/index.html")

def portfolio(request):
    return render(request, "estudio/portfolio.html")