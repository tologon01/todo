from django.shortcuts import render, HttpResponse
from .models import ToDo


def test(request):
    todo_list = ToDo.objects.all() 
    return render(request, "index.html", {"todo_list": todo_list} )

def testing(request):
    todo_list = ToDo.objects.all() 
    return render(request, "test.html", {"todo_list": todo_list} )

def product(request):
    return HttpResponse("This is my first page")

def second(request):
    return HttpResponse("hello test2")
