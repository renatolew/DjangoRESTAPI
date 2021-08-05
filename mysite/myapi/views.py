from rest_framework import viewsets

from .serializers import HeroSerializer, PokemonSerializer
from .models import Hero, Pokemon

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all().order_by('name')
    serializer_class = PokemonSerializer