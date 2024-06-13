from django_filters import FilterSet, DateFilter, CharFilter, ModelChoiceFilter
from django.forms import DateInput
from .models import Post, Author

class PostFilter(FilterSet):
    title = CharFilter(
        label='Содержит',
        lookup_expr='icontains'
    )
    author = ModelChoiceFilter(
        queryset=Author.objects.all(),
        lookup_expr='exact',
        label='Автор',
        empty_label='Все авторы'
    )
    created_at = DateFilter(
        field_name = 'created_at',
        widget = DateInput(attrs={'type': 'date'}),
        label= 'Дата',
        lookup_expr='date__gte'
    )
    class Meta:

        model = Post
        fields = []