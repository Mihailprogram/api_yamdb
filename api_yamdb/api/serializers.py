from rest_framework import serializers
from rest_framework.serializers import (CharField, IntegerField,
                                        ModelSerializer, SlugRelatedField,)

from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from reviews.models import Category, Comment, Genre, Review, Title, User
from reviews.validators import ValidateUsername


class RegistrationSerializer(serializers.Serializer, ValidateUsername):
    """Сериализатор регистрации User"""

    username = serializers.CharField(required=True, max_length=150)
    email = serializers.EmailField(required=True, max_length=254)


class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )


class NotAdminSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )
        read_only_fields = ('role', )


class GetTokenSerializer(ModelSerializer):
    username = CharField(required=True)
    confirmation_code = CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        lookup_field = 'slug'
        fields = ('name', 'slug')


class CategorySerializer(ModelSerializer):
    class Meta:
        exclude = ('id', )
        model = Category
        lookup_field = 'slug'


class TitleWriteSerializer(ModelSerializer):
    category = SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )
    genre = SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True
    )

    class Meta:
        fields = fields = ('id', 'name', 'year',
                           'description', 'genre', 'category')
        model = Title


class TitleReadSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)
    rating = IntegerField(read_only=True, default=1)

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description', 'genre', 'category',
                  'rating')


class ReviewSerializer(ModelSerializer):
    title = SlugRelatedField(
        slug_field='name',
        read_only=True
    )
    author = SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    def validate_score(self, value):
        if 0 > value > 10:
            raise ValidationError('Оценка должна быть по 10-бальной шкале!')
        return value

    def validate(self, data):
        request = self.context['request']
        title_id = self.context.get('view').kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        if (request.method == 'POST'
            and Review.objects.filter(
                title=title, author=request.user).exists()):
            raise ValidationError('Вы можете оставить только один отзыв!')
        return data

    class Meta:
        fields = ('id', 'text', 'title', 'author', 'score', 'pub_date')
        model = Review


class CommentSerializer(ModelSerializer):
    review = SlugRelatedField(slug_field='text', read_only=True)
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'pub_date', 'author', 'review')
        model = Comment
