from django.db import models
from rest_framework import serializers
from drf_extra_fields import fields


class Image(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField()


class ImageSerialiser(serializers.ModelSerializer):
    image = fields.Base64ImageField(required=True)

    class Meta:
        model = Image
        fields = (
            'id',
            'name',
            'image',
        )
