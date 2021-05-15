from .models import Image, ImageSerialiser
from rest_framework import viewsets


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerialiser
