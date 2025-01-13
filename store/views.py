from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from store.models import Category
from store.serializers import CategorySerializer, FilterRequestSerializer


class CategoryViewSet(GenericViewSet):
    """
    Пример класса для написания кастомных эедпоинтов
    """

    @extend_schema(
        parameters=[FilterRequestSerializer],
        summary="Список Категорий",
        tags=["Категории"],
    )
    @action(detail=False, url_path="all", methods=["GET"])
    def object_all(self, request):
        """
        Список Категорий
        :param request:
        :return:
        """
        serializer = FilterRequestSerializer(data=request.query_params)  # отправляем параметры запроса в схему
        serializer.is_valid(raise_exception=True)  # проверяем на валидность

        text_search = serializer.data.get("textSearch")

        # Фильтрация категорий по имени
        category = Category.objects.filter(name=text_search).first()

        if category is not None:
            # Если категория найдена, сериализуем ее
            category_serializer = CategorySerializer(category)  # Используем сериализатор для категории
            return Response(category_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)


class CategoryModelViewSet(ModelViewSet):
    """
    Класс для взаимодействия с таблицей из БД
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
