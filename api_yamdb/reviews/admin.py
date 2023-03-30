from django.contrib.admin import register, ModelAdmin

from .models import Category, Comment, Genre, Review, Title, User


@register(User)
class UserAdmin(ModelAdmin):
    list_display = (
        'username',
        'email',
        'role',
        'bio',
        'first_name',
        'last_name',
        'confirmation_code'
    )
    search_fields = ('username', 'role')
    list_filter = ('username', )
    empty_value_display = '-пусто-'


@register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ('review', 'text', 'author', 'pub_date')
    search_fields = ('review', )
    list_filter = ('review', )
    empty_value_display = '-пусто-'


@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', )
    list_filter = ('name', )
    empty_value_display = '-пусто-'


@register(Review)
class ReviewAdmin(ModelAdmin):
    list_display = ('title', 'text', 'author', 'score')
    search_fields = ('pub_date', )
    list_filter = ('pub_date', )
    empty_value_display = '-пусто-'


@register(Genre)
class GenreAdmin(ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', )
    list_filter = ('name', )
    empty_value_display = '-пусто-'


@register(Title)
class TitleAdmin(ModelAdmin):
    list_display = ('name', 'year', 'category', 'description')
    search_fields = ('name', )
    list_filter = ('name', )
    empty_value_display = '-пусто-'
