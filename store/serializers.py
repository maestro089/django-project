from rest_framework import serializers
from rest_framework.fields import CharField
from rest_framework.serializers import Serializer

from store.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class FilterRequestSerializer(Serializer):
    textSearch = CharField(default="test", required=False)
