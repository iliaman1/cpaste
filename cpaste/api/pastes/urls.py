from django.urls import path

from apps.paste.views import PasteViewSet

urlpatterns = [
    path('pastelist/', PasteViewSet.as_view({'get': 'list'}), name='paste-list'),
    path('paste/<int:pk>', PasteViewSet.as_view({'get': 'retrieve'}), name='paste')
]
