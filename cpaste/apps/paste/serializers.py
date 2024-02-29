from rest_framework import serializers
from .models import Paste


class PasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paste
        fields = ('title', 'category', 'text')
