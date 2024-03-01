from django.urls import path, include
from rest_framework import routers

from apps.paste.views import PasteViewSet


router = routers.SimpleRouter()
router.register(r'paste', PasteViewSet)

urlpatterns = [
    path('', include(router.urls))
]
