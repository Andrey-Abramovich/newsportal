from django_filters import FilterSet, DateFilter, CharFilter,ModelMultipleChoiceFilter  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post, Author
from django.forms import DateInput
import django

# создаём фильтр
class PostFilter(FilterSet):
    dateCreation = DateFilter('dateCreation',
        label = 'дата создания поста',
        # method='gt', не разобрался
        lookup_expr='icontains',
        widget = django.forms.DateInput(attrs={'type': 'date'}),
    )

    title = CharFilter('title',
    label ='Заголовок содержит:',
    lookup_expr ='icontains',
    )

    author = ModelMultipleChoiceFilter('author',
    label ='Автор:',
    lookup_expr ='exact',
    queryset = Author.objects.all()
    )
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) информация о товарах



