from django.core.management.base import BaseCommand, CommandError
from news.models import Post, Category

class Command(BaseCommand):
    help = 'delete all news at category'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        self.stdout.write(f'Вы правда хотите удалить все статьи в категории {options["category"]}? yes/no  ')
        answer = input()

        if answer == 'yes':
            try:
                category_del = Category.objects.get(name=options['category'])
                Post.objects.filter(postcategory__category_across__name=category_del.name).delete()
                self.stdout.write(self.style.SUCCESS(
                    f'Succesfully deleted all news from category {category_del.name}'))  # в случае неправильного подтверждения говорим, что в доступе отказано
            except Post.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Could not find category {category_del.name}'))


        else:
            self.stdout.write(self.style.ERROR('Отменено'))

