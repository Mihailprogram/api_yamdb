from rest_framework import serializers
from .models import Reviews, Comments


class ReviewsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'author','score','pub_date')
        model = Reviews
