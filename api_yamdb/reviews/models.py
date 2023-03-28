from django.contrib.auth import get_user_model
from django.db import models
from titles.models import Title
from user.models import CustomUser

User = get_user_model()


class Reviews(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='автор'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='произведения'
    )

    def __str__(self):
        return self.text


class Comments:
    reviews = models.ForeignKey(
        Reviews,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
