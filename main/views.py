from django.shortcuts import render, HttpResponse



def test(request):
    return render(request, "index.html")

def product(request):
    return HttpResponse("This is my first page")

def second(request):
    return HttpResponse("hello test2")

