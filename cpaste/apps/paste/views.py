from rest_framework.viewsets import ModelViewSet
from .serializers import PasteSerializer
from .models import Paste


class PasteViewSet(ModelViewSet):
    serializer_class = PasteSerializer
    queryset = Paste.objects.all()
