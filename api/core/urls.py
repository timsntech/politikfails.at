from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SnippetViewSet, PolitikerViewSet

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'politiker', PolitikerViewSet)

urlpatterns = [
    path("", include(router.urls))
]