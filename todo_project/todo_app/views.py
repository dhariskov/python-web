from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.http import require_POST

from todo_app.forms import TodoForm
from todo_app.models import Todo


def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'index.html', context=context)


def create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = Todo(title=form.cleaned_data['title'], description=form.cleaned_data['description'])
            todo.save()
            return redirect('create_todo')
    form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'create.html', context=context)


def update(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == "GET":
        form = TodoForm(initial=todo.__dict__)
        context = {
            'form': form,
        }
        return render(request, 'edit.html', context=context)
    else:
        form = TodoForm(request.POST)
        if form.is_valid():
            todo.title = form.cleaned_data['title']
            todo.description = form.cleaned_data['description']
            todo.save()
            return redirect('index')
        return redirect('update_todo')


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('index')
