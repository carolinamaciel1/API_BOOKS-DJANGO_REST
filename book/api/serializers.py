from rest_framework.serializers import ModelSerializer
from book.models import Book, CopyBook, RentBook


class BookSerializer(ModelSerializer):
    """
    Serializer Book fields
    """
    class Meta:
        model = Book
        fields = '__all__'


class CopyBookSerializer(ModelSerializer):
    """
    Serializer CopyBook fields
    """
    class Meta:
        model = CopyBook
        fields = '__all__'


class RentBookSerializer(ModelSerializer):
    """
    Serializer RentBook fields
    """
    class Meta:
        model = RentBook
        fields = '__all__'



