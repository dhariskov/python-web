from django.shortcuts import render, redirect

# Create your views here.
from book_app.forms import BookForm
from book_app.models import Book


def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'index.html', context=context)


def create_edit_modelform(request, book, template):
    if request.method == 'GET':
        context = {
            'form': BookForm(instance=book)
        }
        return render(request, f'{template}', context=context)
    else:
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, f'{template}', context=context)


def create(request):
    return create_edit_modelform(request, Book(), 'create.html')
    # if request.method == 'GET':
    #     context = {
    #         'form': BookForm(),
    #     }
    #     return render(request, 'create.html', context=context)
    # else:
    #     form = BookForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('index')
    #     context = {
    #         'form': form
    #     }
    #     return render(request, 'create.html', context=context)


def edit(request, pk):
    return create_edit_modelform(request, Book.objects.get(pk=pk), 'edit.html')
    # book = Book.objects.get(pk=pk)
    # if request.method == "GET":
    #     context={
    #         'form': book
    #     }
    #     return render(request, 'edit.html', context)
    # else:
    #     form = BookForm(request.POST, instance=book)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('index')
    #     context = {
    #         'form': form
    #     }
    #     return render(request, 'edit.html', context=context)
