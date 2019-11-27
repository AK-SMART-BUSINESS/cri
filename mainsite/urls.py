from django.urls import path

from . import views

app_name = 'mainsite'
urlpatterns = [
    path('', views.index, name='index'),
    path('departements', views.departements, name="departements"),
    path('departement/recherche', views.recherche, name="recherche"),
    path('departement/formation', views.formation, name="formation"),
    path('departement/ingenierie', views.ingenierie, name="ingenierie"),
    path('departement/communication', views.communication, name="communication"),
    path('projets', views.projets, name="projets"),
    path('expertises', views.expertises, name="expertises"),
    path('partenariats', views.partenariats, name="partenariats"),
    path('contacts', views.contacts, name="contacts"),
    path('mot-du-directeur', views.manager, name="manager"),
    path('vision-but-objectifs', views.vision_but_objectifs, name="vision_but_objectifs"),
    path('mission', views.mission, name="mission"),
    path('nos-valeurs', views.nos_valeurs, name="nos_valeurs")
    # path('apropos', views.about, name='about')
]