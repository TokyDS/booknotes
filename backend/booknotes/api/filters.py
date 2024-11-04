from django_filters import rest_framework as filters

from .models import Book, Note

class BookFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    # author_first_name = filters.CharFilter(field_name='author__first_name', lookup_expr='icontains')
    
    class Meta:
        model = Book
        fields = ['title', 'author']
        
class NoteFilter(filters.FilterSet):
    book = filters.CharFilter(field_name='book__title', lookup_expr='icontains')
    class Meta:
        model = Note
        fields = ['book', 'tag']
        