from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    template = "core/home.html"
    return render(request, template)

def about(request):
    template = "core/about.html"
    return render(request, template)

def store(request):
    template = "core/store.html"
    return render(request, template)
