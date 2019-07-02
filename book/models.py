from django.db import models
from django.contrib.auth.models import User

"""
    Book: all atributtes of book model
"""


class Book(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    author = models.CharField(max_length=200, null=False, blank=False)
    publishing_company = models.CharField(max_length=150, null=True, blank=True)
    registration_date = models.DateField()

    def __str__(self):
        return self.name


"""
    CopyBook: all atributtes of copy book model
"""


class CopyBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False, blank=False)
    date_register = models.DateField()

    def __str__(self):
        return self.book


"""
    RentBook: all atributtes of rent book model
"""


class RentBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    book = models.ForeignKey(CopyBook, on_delete=models.CASCADE, null=False, blank=False)
    date_initial_rent = models.DateField()
    delivery_date_forecast = models.DateField()
    date_devolution = models.DateField()

    def __str__(self):
        return self.book
