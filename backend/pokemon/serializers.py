from rest_framework import serializers
from .models import Tipo, Pokemon, PokemonEspecie, Equipo
from django.contrib.auth.models import User


class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ["id", "nombre"]

class PokemonEspecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonEspecie
        fields = ["id", "nombre", "numero_pokedex", "primer_tipo", "segundo_tipo"]

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ["id", "apodo", "usuario", "naturaleza", "especie", "nivel", "iv_hp", "iv_ataque", "iv_defensa", 
                  "iv_ataque_especial", "iv_defensa_especial", "iv_velocidad", "ev_hp", "ev_ataque", "ev_defensa",
                  "ev_ataque_especial", "ev_defensa_especial", "ev_velocidad"]

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ["id", "nombre", "usuario", "pokemones"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)