from rest_framework import viewsets
from titles.models import Genre, Category, Title
from .serializers import (
    GenreSerializer,
    CategorySerializer,
    TitleSerializer
)

TBA_PERMISSION_CLASS = None


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (TBA_PERMISSION_CLASS,)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (TBA_PERMISSION_CLASS,)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (TBA_PERMISSION_CLASS,)
