from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SnippetViewSet, PoliticianViewSet, CategoryViewSet, PartyViewSet

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'politicians', PoliticianViewSet)
router.register(r'parties', PartyViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path("", include(router.urls))
]