from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Tipo(models.Model):
    nombre = models.CharField(max_length=100)

class PokemonEspecie(models.Model):
    nombre = models.CharField(max_length=100)
    numero_pokedex = models.IntegerField(unique=True)

    primer_tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, related_name="especies_tipo_principal")
    segundo_tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, related_name="especies_tipo_secundario", blank=True, null=True)

class Pokemon(models.Model):

    apodo = models.CharField(max_length=100, blank=True)

    usuario = models.ForeignKey(User, 
        on_delete=models.CASCADE, 
        related_name="pokemones"
        )
    
    naturaleza = models.CharField(max_length=100)

    especie = models.ForeignKey(PokemonEspecie,
         on_delete=models.PROTECT,
         related_name="ejemplares"
        )

    nivel = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(100)])

    iv_hp = models.PositiveSmallIntegerField(
        validators=[
        MinValueValidator(0),
        MaxValueValidator(31)])
    
    iv_ataque = models.PositiveSmallIntegerField(
        validators=[
        MinValueValidator(0),
        MaxValueValidator(31)])
    
    iv_defensa = models.PositiveSmallIntegerField(
        validators=[
        MinValueValidator(0),
        MaxValueValidator(31)])
    
    iv_ataque_especial = models.PositiveSmallIntegerField(
        validators=[
        MinValueValidator(0),
        MaxValueValidator(31)])
    
    iv_defensa_especial = models.PositiveSmallIntegerField(
        validators=[
        MinValueValidator(0),
        MaxValueValidator(31)])
    
    iv_velocidad = models.PositiveSmallIntegerField(
        validators=[
        MinValueValidator(0),
        MaxValueValidator(31)])
    

    ev_hp = models.PositiveSmallIntegerField(
        validators=[
        MinValueValidator(0),
        MaxValueValidator(252)])
    
    ev_ataque = models.PositiveSmallIntegerField(
        validators=[
        MinValueValidator(0),
        MaxValueValidator(252)])
    
    ev_defensa = models.PositiveSmallIntegerField(
        validators=[
        MinValueValidator(0),
        MaxValueValidator(252)])
    
    ev_ataque_especial = models.PositiveSmallIntegerField(
        validators=[
        MinValueValidator(0),
        MaxValueValidator(252)])
    
    ev_defensa_especial = models.PositiveSmallIntegerField(
        validators=[
        MinValueValidator(0),
        MaxValueValidator(252)])
    
    ev_velocidad = models.PositiveSmallIntegerField(
        validators=[
        MinValueValidator(0),
        MaxValueValidator(252)])
    


class ModificadorTipo(models.Model):
    factor_de_modificacion = models.FloatField()


    atacante = models.ForeignKey (
        Tipo,
        on_delete=models.PROTECT,
        related_name="ataques"
    )

    defensor = models.ForeignKey (
        Tipo,
        on_delete=models.PROTECT,
        related_name="defensas"
    )

    class Meta:
            constraints = [
                models.UniqueConstraint(
                    fields=["atacante","defensor"], 
                    name="tipo_unico")]

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name="equipos"
    )
    pokemones = models.ManyToManyField(Pokemon, related_name="equipos")






