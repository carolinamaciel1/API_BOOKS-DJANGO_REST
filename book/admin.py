from django.contrib import admin
from book.models import Book,CopyBook,RentBook

admin.site.register(Book)
admin.site.register(CopyBook)
admin.site.register(RentBook)

