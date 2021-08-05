from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"heroes", views.HeroViewSet)
router.register(r"pokemons", views.PokemonViewSet)

# Make automatic routing for the API to adjust URLs accordingly.
# Adding login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]