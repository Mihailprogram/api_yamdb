from rest_framework import viewsets
from .models import Review, Comment, Title
from .serializers import ReviewsSerializer, CommentsSerializer
from django.shortcuts import get_object_or_404


class ReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewsSerializer

    def get_queryset(self):
        title = Review.objects.filter(title=self.kwargs.get('title_id'))
        return title

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer

    def get_queryset(self):
        review = Comment.objects.filter(reviews=self.kwargs.get('review_id'))
        return review

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)
