from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import default_token_generator
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import (CASCADE, SET_NULL, CharField, DateTimeField,
                              EmailField, ForeignKey, IntegerField,
                              ManyToManyField, Model, SlugField, TextField,
                              UniqueConstraint,)
from django.db.models.signals import post_save
from django.dispatch import receiver

from .validators import validate_username, validate_year

USER = 'user'
ADMIN = 'admin'
MODERATOR = 'moderator'

ROLE_CHOICES = [
    (USER, USER),
    (ADMIN, ADMIN),
    (MODERATOR, MODERATOR),
]


class User(AbstractUser):
    username = CharField(
        validators=(validate_username,),
        max_length=150,
        unique=True,
        blank=False,
        null=False
    )
    email = EmailField(
        max_length=254,
        unique=True,
        blank=False,
        null=False
    )
    role = CharField(
        'роль',
        max_length=20,
        choices=ROLE_CHOICES,
        default=USER,
        blank=True
    )
    bio = TextField(
        'биография',
        blank=True,
    )
    first_name = CharField(
        'имя',
        max_length=150,
        blank=True
    )
    last_name = CharField(
        'фамилия',
        max_length=150,
        blank=True
    )
    confirmation_code = CharField(
        'код подтверждения',
        max_length=255,
        null=True,
        blank=False,
        default='XXXX'
    )

    @property
    def is_user(self):
        return self.role == USER

    @property
    def is_admin(self):
        return self.role == ADMIN or self.is_superuser or self.is_staff

    @property
    def is_moderator(self):
        return self.role == MODERATOR

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


@receiver(post_save, sender=User)
def post_save(sender, instance, created, **kwargs):
    if created:
        confirmation_code = default_token_generator.make_token(
            instance
        )
        instance.confirmation_code = confirmation_code
        instance.save()


class Category(Model):
    name = CharField('Категория', max_length=100)
    slug = SlugField('Слаг категории', unique=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name} {self.name}'


class Genre(Model):
    name = CharField('Жанр', max_length=100)
    slug = SlugField('Слаг жанра', unique=True, db_index=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return f'{self.name} {self.name}'


class Title(Model):
    name = CharField('Название', max_length=100, db_index=True)
    year = IntegerField('Год', validators=(validate_year, ))
    category = ForeignKey(
        Category,
        on_delete=SET_NULL,
        related_name='titles',
        verbose_name='Категория',
        null=True,
        blank=True
    )
    description = TextField('Описание', null=True, blank=True)
    genre = ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='жанр'
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class Review(Model):
    title = ForeignKey(
        Title,
        on_delete=CASCADE,
        related_name='reviews',
        verbose_name='Произведение'
    )
    text = CharField(max_length=255)
    author = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
    score = IntegerField(
        'Оценка',
        validators=(
            MinValueValidator(1),
            MaxValueValidator(10)
        ),
        error_messages={'validators': 'Оценка должна быть от 1 до 10!'}
    )
    pub_date = DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            UniqueConstraint(
                name='unique review',
                fields=('title', 'author')
            )
        ]
        ordering = ('-pub_date', )

    def __str__(self):
        return self.text


class Comment(Model):
    review = ForeignKey(
        Review,
        on_delete=CASCADE,
        related_name='comments',
        verbose_name='Отзыв'
    )
    text = TextField('Комментарий')
    author = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    pub_date = DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
