from rest_framework.serializers import ModelSerializer
from book.models import Book, CopyBook,RentBook

"""
    Serializer Book
"""


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


"""
    Serializer CopyBook
"""


class CopyBookSerializer(ModelSerializer):
    class Meta:
        model = CopyBook
        fields = '__all__'


"""
    Serializer RentBook
"""


class RentBookSerializer(ModelSerializer):
    class Meta:
        model = RentBook
        fields = '__all__'



