from .models import Genre, Category, Title
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'

    def __str__(self):
        return self.name


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

    def __str__(self):
        return self.name


class TitleSerializer(serializers.ModelSerializer):
    category = SlugRelatedField(
        slug_field='category',
        queryset=Category.objects.all()
    )
    genre = SlugRelatedField(
        slug_field='genre',
        queryset=Genre.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Title
