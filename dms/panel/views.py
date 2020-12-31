from django.shortcuts import render


def index(request):
    return render(request, "panel/index.html")
