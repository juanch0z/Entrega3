from rest_framework import viewsets
from .serializer import usuarioSerializer
from .models import usuarios


class usuarioViewSet(viewsets.ModelViewSet):
    queryset= usuarios.objects.all()
    serializer_class = usuarioSerializer
