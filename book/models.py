from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    """
    A class used to represent book in a library

    Attributes
    ----------
    book's name: str
        name of book
    book's author str
        name of author of the book
    book's publishing company: str
        name of pushing company of the book
    book's registration date: obj
        date of registration of book in the library
    """
    name_book = models.CharField(max_length=200, null=False, blank=False)
    author_book = models.CharField(max_length=200, null=False, blank=False)
    publishing_company = models.CharField(max_length=150, null=True, blank=True)
    registration_date = models.DateField()


class CopyBook(models.Model):
    """
    A class used to represent a copy book in a library

    Attributes
    ----------
    book's: str
        foreign key to book
    book's date register: obj
        date of register copy book in the library
    book's edition: int
        number edition of the book
    """
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False, blank=False)
    date_register = models.DateField()
    edition = models.IntegerField(null=False, blank=True)


class RentBook(models.Model):
    """
    A class used to represent a rent book in a library

    Attributes
    ----------
    library's librarian: str
        foreign key to user admin
    name's user: str
        name the people how rent book in the library
    book's rental date: obj
        date of the people rent a book in the library
    book's delivery date forecast: obj
        date forecast of devolution of the book in the library
    book's devolution date: obj
        the real date of devolution of the book
    """
    librarian = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank= True)
    book = models.ForeignKey(CopyBook, on_delete=models.CASCADE, null=False, blank=False)
    date_initial_rent = models.DateField()
    delivery_date_forecast = models.DateField()
    date_devolution = models.DateField(null=True, blank=True)


