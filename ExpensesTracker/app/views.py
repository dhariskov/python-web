from django.shortcuts import render, redirect

# Create your views here.
from app.forms import ProfileForm, ExpenseForm
from app.models import Profile, Expense


def index(request):
    if not Profile.objects.all():
        form = ProfileForm()
        if request.method == 'GET':
            context = {
                'form': form,
            }
            return render(request, 'home-no-profile.html', context=context)
        else:
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        context = {
            'form': form
        }
        return render(request, 'home-no-profile.html', context=context)
    form = ProfileForm(Profile.objects.all())
    budget = Profile.objects.all()[0].budget
    expenses = Expense.objects.all()
    budget_left = budget - sum([ex.price for ex in expenses])
    context = {
        'form': form,
        'budget': budget,
        'expenses': expenses,
        'budget_left': budget_left,
    }
    return render(request, 'home-with-profile.html', context=context)


def create(request):

    if request.method == 'GET':
        form = ExpenseForm(initial={'profile': Profile.objects.all()[0]})
        context = {
            'form': form,
        }
        return render(request, 'expense-create.html', context=context)
    else:
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form': form,
        }
        return render(request, 'expense-create.html', context=context)


def edit(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        form = ExpenseForm(instance=expense)
        context = {
            'form': form,
        }
        return render(request, 'expense-edit.html', context)
    else:
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form': form,
        }
        return render(request, 'expense-edit.html', context)


# todo make read only filed of the form
def delete(request, pk):
    expense = Expense.objects.get(pk=pk)
    title = expense.title
    link = expense.image_url
    description = expense.description
    price = expense.price
    if request.method == 'GET':
        form = ExpenseForm(instance=expense)
        context = {
            'form': form,
            'title': title,
            'link': link,
            'description': description,
            'price': price,
        }
        return render(request, 'expense-delete.html', context)
    else:
        expense.delete()
        return redirect('index')


def profile(request):
    name = Profile.objects.all()[0].first_name + ' ' + Profile.objects.all()[0].last_name
    budget = Profile.objects.all()[0].budget
    expenses = Expense.objects.all()
    budget_left = budget - sum([ex.price for ex in expenses])
    context = {
        'budget_left': budget_left,
        'name': name
    }
    return render(request, 'profile.html', context=context)


def profile_edit(request):
    profile = Profile.objects.all()[0]
    if request.method == 'GET':
        context = {
            'form': ProfileForm(instance=profile)
        }
        return render(request, 'profile-edit.html', context=context)
    else:
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        context = {
            'form': form,
        }
        return render(request, 'profile-edit.html', context=context)


def profile_delete(request):
    if request.method == 'GET':
        return render(request, 'profile-delete.html')
    else:
        profile = Profile.objects.all()[0]
        profile.delete()
        for ex in Expense.objects.all():
            ex.delete()
        return redirect('index')
