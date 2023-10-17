from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    isbn = models.CharField(max_length=50)
    publisher = models.CharField(max_length=200)
    pages = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
class Member(models.Model):
    name = models.CharField(max_length=50)
    outstanding_debt = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    rent_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        if self.return_date:
            return f"{self.member.name} returned {self.book.title}"
        return f"{self.member.name} issued {self.book.title}"    