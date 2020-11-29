from django.shortcuts import render, redirect

# Create your views here.
from pets.forms import CreatePetForm, CommentForm
from pets.models import Pet, Like, Comment


def pet_all(request):
    context = {
        'pets': Pet.objects.all(),
    }
    return render(request, 'pets/pet_list.html', context=context)


def pet_detail(request, pk):
    if request.method == 'GET':
        context = {
            'pet': Pet.objects.get(pk=pk),
            'form': CommentForm(),
        }
        return render(request, 'pets/pet_detail.html', context=context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(comment=form.cleaned_data['comment'])
            pet = Pet.objects.get(pk=pk)
            comment.pet = pet
            comment.save()
            return redirect('details', pk)
        context = {
            'pet': Pet.objects.get(pk=pk),
            'form': CommentForm(),
        }
        return render(request, 'pets/pet_detail.html', context=context)


def like(request, pk):
    pet = Pet.objects.get(pk=pk)
    like_object = Like()
    like_object.pet = pet
    like_object.save()
    return redirect('details', pk)


def create(request):
    if request.method == "GET":
        context = {
            'form': CreatePetForm(),
        }
        return render(request, 'pets/pet_create.html', context=context)
    else:
        form = CreatePetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pets')
    context = {
        'form': form
    }
    return render(request, 'pets/pet_create.html', context=context)


def edit(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form': CreatePetForm(instance=pet)
        }
        return render(request, 'pets/pet_edit.html', context=context)
    else:
        form = CreatePetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pets')
    context = {
        'form': form,
    }
    return render(request, 'pets/pet_edit.html', context=context)


def delete(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        pet_name = pet.name
        context = {
            'pet_name': pet_name,
        }
        return render(request, 'pets/pet_delete.html', context=context)
    else:
        if request.method == 'POST':
            pet.delete()
            return redirect('pets')
        context = {
            'form': CreatePetForm(instance=pet)
        }
        return render(request, 'pets/pet_detail.html', context=context)


