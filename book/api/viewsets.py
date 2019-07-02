from rest_framework.viewsets import ModelViewSet
from book.models import Book, CopyBook,RentBook
from book.api.serializers import BookSerializer,CopyBookSerializer,RentBookSerializer

"""
    ViewSet Book
"""


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


"""
    ViewSet CopyBook
"""


class CopyBookViewSet(ModelViewSet):
    queryset = CopyBook.objects.all()
    serializer_class = CopyBookSerializer


"""
    ViewSet RentBook
"""


class RentBookViewSet(ModelViewSet):
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializer

