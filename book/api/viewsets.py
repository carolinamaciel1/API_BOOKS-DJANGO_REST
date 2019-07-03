from rest_framework.viewsets import ModelViewSet
from book.models import Book, CopyBook, RentBook
from book.api.serializers import BookSerializer, CopyBookSerializer, RentBookSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class BookViewSet(ModelViewSet):
    """
    BookViewSet returns all books in the library, we can filter through  book's name,
    book's author and book's registration date, also we can order by book's registration.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ('id', 'name_book', 'author_book', 'registration_date')
    ordering_fields = ('registration_date',)
    permission_classes = (IsAuthenticated, IsAdminUser )


class CopyBookViewSet(ModelViewSet):
    """
    CopyBookViewSet returns all book's copy in the library, we can filter through
    book's edition, book's registration date, book's name and book's author.
    """
    queryset = CopyBook.objects.all()
    serializer_class = CopyBookSerializer
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ('edition', 'date_register')
    ordering_fields = ('edition', 'date_register',)
    permission_classes = (IsAuthenticated, IsAdminUser)


class RentBookViewSet(ModelViewSet):
    """
    RentBookViewSet returns all book's rent in the library, we can filter through
    name of the person who rented the book and by the expected delivery date of books.
    """
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializer
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ('^name', 'delivery_date_forecast')
    lookup_field = 'name'
    ordering_fields = ('name', 'delivery_date_forecast')
    permission_classes = (IsAuthenticated, IsAdminUser)




