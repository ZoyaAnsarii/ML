from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Polls App</h1>")
def about(request):
    return HttpResponse("<h1>Pakistan Zindabad!</h1>")