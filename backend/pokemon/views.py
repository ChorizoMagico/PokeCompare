
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import PokemonEspecie, Pokemon, Tipo, ModificadorTipo, Equipo
from .serializers import PokemonSerializer, PokemonEspecieSerializer, EquipoSerializer, UserSerializer

# Create your views here.

@api_view(["GET"])
def ObtenerEspeciesVista(request):
    especies =  PokemonEspecie.objects.all()
    serializer = PokemonEspecieSerializer(especies, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


class EquiposVista(APIView):

    def get(self, request):

        equipos = Equipo.objects.filter(usuario=request.user)
        serializer = EquipoSerializer(equipos, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = EquipoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(usuario=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PokemonesVista(APIView):

    def post(self, request):

        serializer = PokemonSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(usuario=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):

        pokemones = Pokemon.objects.filter(usuario=request.user)
        serializer = PokemonSerializer(pokemones, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



class PokemonIndividualVista(APIView):

    def get(self, request, pokemon_id):

        pokemon = Pokemon.objects.get(id=pokemon_id, usuario=request.user)
        serializer = PokemonSerializer(pokemon)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pokemon_id):

        Pokemon.objects.get(id=pokemon_id, usuario=request.user).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pokemon_id):

        pokemon = Pokemon.objects.get(id=pokemon_id, usuario=request.user)

        serializer = PokemonSerializer(pokemon, data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class EquipoIndividualVista(APIView):

    def get(self, request, equipo_id):

        equipo = Equipo.objects.get(id=equipo_id, usuario=request.user)
        serializer = EquipoSerializer(equipo)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, equipo_id):

        Equipo.objects.get(id=equipo_id, usuario=request.user).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, equipo_id):

        equipo = Equipo.objects.get(id=equipo_id, usuario=request.user)
        serializer = EquipoSerializer(equipo, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    