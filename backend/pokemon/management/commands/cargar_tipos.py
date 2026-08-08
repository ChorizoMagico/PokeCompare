from django.core.management.base import BaseCommand
from pokemon.models import Tipo, ModificadorTipo

class Command(BaseCommand):

    def handle(self, *args, **kwargs):


        tipos = ["Agua", "Fuego", "Planta", "Acero", "Bicho", "Dragon", "Electrico", "Fantasma", "Hada", 
                 "Lucha", "Hielo", "Normal", "Psiquico", "Roca", "Siniestro", "Tierra", "Veneno", "Volador"]

        tipos_creados = {}

        for tipo in tipos:
            tipos_creados[tipo], _ = Tipo.objects.get_or_create(nombre=tipo)

        modificaciones = [
    # Acero
    ("Acero", "Hielo", 2),
    ("Acero", "Roca", 2),
    ("Acero", "Hada", 2),
    ("Acero", "Acero", 0.5),
    ("Acero", "Fuego", 0.5),
    ("Acero", "Agua", 0.5),
    ("Acero", "Electrico", 0.5),

    # Agua
    ("Agua", "Fuego", 2),
    ("Agua", "Tierra", 2),
    ("Agua", "Roca", 2),
    ("Agua", "Agua", 0.5),
    ("Agua", "Planta", 0.5),
    ("Agua", "Dragon", 0.5),

    # Bicho
    ("Bicho", "Planta", 2),
    ("Bicho", "Psiquico", 2),
    ("Bicho", "Siniestro", 2),
    ("Bicho", "Fuego", 0.5),
    ("Bicho", "Lucha", 0.5),
    ("Bicho", "Veneno", 0.5),
    ("Bicho", "Volador", 0.5),
    ("Bicho", "Fantasma", 0.5),
    ("Bicho", "Acero", 0.5),
    ("Bicho", "Hada", 0.5),

    # Dragon
    ("Dragon", "Dragon", 2),
    ("Dragon", "Acero", 0.5),
    ("Dragon", "Hada", 0),

    # Electrico
    ("Electrico", "Agua", 2),
    ("Electrico", "Volador", 2),
    ("Electrico", "Planta", 0.5),
    ("Electrico", "Electrico", 0.5),
    ("Electrico", "Dragon", 0.5),
    ("Electrico", "Tierra", 0),

    # Fantasma
    ("Fantasma", "Fantasma", 2),
    ("Fantasma", "Psiquico", 2),
    ("Fantasma", "Siniestro", 0.5),
    ("Fantasma", "Normal", 0),

    # Fuego
    ("Fuego", "Planta", 2),
    ("Fuego", "Hielo", 2),
    ("Fuego", "Bicho", 2),
    ("Fuego", "Acero", 2),
    ("Fuego", "Fuego", 0.5),
    ("Fuego", "Agua", 0.5),
    ("Fuego", "Roca", 0.5),
    ("Fuego", "Dragon", 0.5),

    # Hada
    ("Hada", "Lucha", 2),
    ("Hada", "Dragon", 2),
    ("Hada", "Siniestro", 2),
    ("Hada", "Fuego", 0.5),
    ("Hada", "Veneno", 0.5),
    ("Hada", "Acero", 0.5),

    # Hielo
    ("Hielo", "Planta", 2),
    ("Hielo", "Tierra", 2),
    ("Hielo", "Volador", 2),
    ("Hielo", "Dragon", 2),
    ("Hielo", "Fuego", 0.5),
    ("Hielo", "Agua", 0.5),
    ("Hielo", "Hielo", 0.5),
    ("Hielo", "Acero", 0.5),

    # Lucha
    ("Lucha", "Normal", 2),
    ("Lucha", "Hielo", 2),
    ("Lucha", "Roca", 2),
    ("Lucha", "Siniestro", 2),
    ("Lucha", "Acero", 2),
    ("Lucha", "Veneno", 0.5),
    ("Lucha", "Volador", 0.5),
    ("Lucha", "Psiquico", 0.5),
    ("Lucha", "Bicho", 0.5),
    ("Lucha", "Hada", 0.5),
    ("Lucha", "Fantasma", 0),

    # Normal
    ("Normal", "Roca", 0.5),
    ("Normal", "Acero", 0.5),
    ("Normal", "Fantasma", 0),

    # Planta
    ("Planta", "Agua", 2),
    ("Planta", "Tierra", 2),
    ("Planta", "Roca", 2),
    ("Planta", "Fuego", 0.5),
    ("Planta", "Planta", 0.5),
    ("Planta", "Veneno", 0.5),
    ("Planta", "Volador", 0.5),
    ("Planta", "Bicho", 0.5),
    ("Planta", "Dragon", 0.5),
    ("Planta", "Acero", 0.5),

    # Psiquico
    ("Psiquico", "Lucha", 2),
    ("Psiquico", "Veneno", 2),
    ("Psiquico", "Psiquico", 0.5),
    ("Psiquico", "Acero", 0.5),
    ("Psiquico", "Siniestro", 0),

    # Roca
    ("Roca", "Fuego", 2),
    ("Roca", "Hielo", 2),
    ("Roca", "Volador", 2),
    ("Roca", "Bicho", 2),
    ("Roca", "Lucha", 0.5),
    ("Roca", "Tierra", 0.5),
    ("Roca", "Acero", 0.5),

    # Siniestro
    ("Siniestro", "Fantasma", 2),
    ("Siniestro", "Psiquico", 2),
    ("Siniestro", "Lucha", 0.5),
    ("Siniestro", "Siniestro", 0.5),
    ("Siniestro", "Hada", 0.5),

    # Tierra
    ("Tierra", "Fuego", 2),
    ("Tierra", "Electrico", 2),
    ("Tierra", "Veneno", 2),
    ("Tierra", "Roca", 2),
    ("Tierra", "Acero", 2),
    ("Tierra", "Planta", 0.5),
    ("Tierra", "Bicho", 0.5),
    ("Tierra", "Volador", 0),

    # Veneno
    ("Veneno", "Planta", 2),
    ("Veneno", "Hada", 2),
    ("Veneno", "Veneno", 0.5),
    ("Veneno", "Tierra", 0.5),
    ("Veneno", "Roca", 0.5),
    ("Veneno", "Fantasma", 0.5),
    ("Veneno", "Acero", 0),

    # Volador
    ("Volador", "Planta", 2),
    ("Volador", "Lucha", 2),
    ("Volador", "Bicho", 2),
    ("Volador", "Electrico", 0.5),
    ("Volador", "Roca", 0.5),
    ("Volador", "Acero", 0.5),
]


        
        for atacante, defensor, factor in modificaciones:
            ModificadorTipo.objects.get_or_create(factor_de_modificacion = factor,
                                            atacante = tipos_creados[atacante],
                                            defensor = tipos_creados[defensor])