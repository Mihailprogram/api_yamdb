from csv import DictReader

from reviews.models import Category, Comment, Genre, Review, Title, User

from django.conf import settings
from django.core.management import BaseCommand

TABLES = {
    User: 'users.csv',
    Category: 'category.csv',
    Genre: 'genre.csv',
    Title: 'titles.csv',
    Review: 'review.csv',
    Comment: 'comments.csv',
}


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for model, csv_f in TABLES.items():
            print(f'model={model}, file={csv_f}')
            with open(
                f'{settings.BASE_DIR}/static/data/{csv_f}',
                'r',
                encoding='utf-8'
            ) as csv_file:
                reader = DictReader(csv_file)
                if csv_f == 'titles.csv':
                    for data in reader:
                        cat_id = data.get('category')
                        data['category'] = Category.objects.get(id=cat_id)
                        Title.objects.create(**data)
                if csv_f == 'review.csv':
                    for data in reader:
                        print(data)
                        author_id = data['author']
                        data['author'] = User.objects.get(id=author_id)
                        Review.objects.create(**data)
                if csv_f == 'comments.csv':
                    for data in reader:
                        author_id = data['author']
                        data['author'] = User.objects.get(id=author_id)
                        Comment.objects.create(**data)
                model.objects.bulk_create(
                    model(**data) for data in reader
                )
        return True
    