from rest_framework import serializers
from .models import test
class testserializers(serializers.ModelSerializer):
    class Meta:
        model = test
        fields = ['id', 'name', 'description']