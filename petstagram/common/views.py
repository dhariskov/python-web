from django.shortcuts import render


# Create your views here.
def landing_lage(request):
    return render(request, 'landing_page.html')
