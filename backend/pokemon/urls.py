from django.urls import path
from . import views

#api/pokemon/

urlpatterns = [
    path('especies/', views.ObtenerEspeciesVista),
    path('pokemones/', views.PokemonesVista.as_view()),
    path('pokemones/<int:pokemon_id>/', views.PokemonIndividualVista.as_view()),
    path('equipos/', views.EquiposVista.as_view()),
    path('equipos/<int:equipo_id>/', views.EquipoIndividualVista.as_view()),
]
