from rest_framework import serializers

from .models import Hero, Pokemon

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ("id", "name", "alias")

class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = ("id", "name", "type")