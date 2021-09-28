from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SnippetViewSet, PoliticianViewSet, CategoryViewSet, PartyViewSet

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'politiker', PoliticianViewSet)
router.register(r'partei', PartyViewSet)
router.register(r'kategorie', CategoryViewSet)

urlpatterns = [
    path("", include(router.urls))
]