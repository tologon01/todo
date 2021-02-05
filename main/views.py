from django.shortcuts import render, HttpResponse


def homepage(request):
    return HttpResponse("hello world!")

def test(request):
    return render(request, "test.html")

def product(request):
    return HttpResponse("This is my first page")

def second(request):
    return HttpResponse("hello test2")

