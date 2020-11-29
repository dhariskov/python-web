from django.shortcuts import render, redirect

# Create your views here.
from recipes.forms import RecipeForm
from recipes.models import Recipe


def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context=context)


def create(request):
    if request.method == "GET":
        form = RecipeForm()
        context = {
            'form': form
        }
        return render(request, 'create.html', context=context)
    else:
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form': form,
        }
        return render(request, 'create.html', context=context)


def edit(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "GET":
        form = RecipeForm(instance=recipe)
        context = {
            'form': form
        }
        return render(request, 'edit.html', context=context)
    else:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form': form,
        }
        return render(request, 'edit.html', context=context)


def delete(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    # form = RecipeForm(instance=recipe)
    title = recipe.title
    image_url = recipe.image_url
    description = recipe.description
    ingredients = recipe.ingredients
    time = recipe.time
    if request.method == 'GET':
        context = {
            'title': title,
            'image_url': image_url,
            'description': description,
            'ingredients': ingredients,
            'time': time,
        }
        return render(request, 'delete.html', context=context)
    else:
        recipe.delete()
        return redirect('index')


def details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    title = recipe.title
    image_url = recipe.image_url
    description = recipe.description
    ingredients = recipe.ingredients.split(',')
    time = recipe.time
    if request.method == 'GET':
        context = {
            'title': title,
            'image_url': image_url,
            'description': description,
            'ingredients': ingredients,
            'time': time,
            'pk': pk
        }
        return render(request, 'details.html', context=context)
