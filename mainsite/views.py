from django.shortcuts import render, get_object_or_404

from .models import Home, About

# Create your views here.
def index(request):
    homepage = get_object_or_404(Home, publish=1)
    context = {
        'home': homepage
    }
    return render(request, 'mainsite/index.html', context)

def about(request):
    return render(request, 'mainsite/aboutus.html')