from django.shortcuts import render, HttpResponse, redirect
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

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(testing)