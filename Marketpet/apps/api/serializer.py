from rest_framework import serializers
from .models import usuarios


class usuarioSerializer (serializers.ModelSerializer):
    class Meta:
        model = usuarios
        fields ='__all__'