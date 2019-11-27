from django.shortcuts import render, get_object_or_404

from .models import Home, About

# Create your views here.
def index(request):
    homepage = get_object_or_404(Home, publish=1)
    context = {
        'home': homepage
    }
    return render(request, 'mainsite/index.html', context)

def departements(request):
    return render(request, 'mainsite/departement.html')

def projets(request):
    return render(request, 'mainsite/projet.html')

def expertises(request):
    return render(request, 'mainsite/expertise.html')

def partenariats(request):
    return render(request, 'mainsite/partenaire.html')

def contacts(request):
    return render(request, 'mainsite/contact.html')

def recherche(request):
    return render(request, 'mainsite/recherche.html')

def formation(request):
    return render(request, 'mainsite/formation.html')

def ingenierie(request):
    return render(request, 'mainsite/ingenierie.html')

def communication(request):
    return render(request, 'mainsite/communication.html')

def manager(request):
    return render(request, 'mainsite/manager.html')

def vision_but_objectifs(request):
    return render(request, 'mainsite/vbo.html')

def mission(request):
    return render(request, 'mainsite/mission.html')

def nos_valeurs(request):
    return render(request, 'mainsite/valeurs.html')
