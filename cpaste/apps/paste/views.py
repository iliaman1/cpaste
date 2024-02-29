from rest_framework.generics import ListCreateAPIView
from .serializers import PasteSerializer


class PasteListCreate(ListCreateAPIView):
    serializer_class = PasteSerializer
