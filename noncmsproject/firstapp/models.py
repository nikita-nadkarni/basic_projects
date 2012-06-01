from django.db import models

# Create your models here.

class Book(models.Model):
    BOOK_CHOICES = (
        (u'F', u'Fiction'),
        (u'NF', u'NonFiction'),                
    )
    title = models.CharField(max_length=100)
    len = models.IntegerField()
    type = models.CharField(max_length=2, choices=BOOK_CHOICES)
    
    def __unicode__(self):
        return self.title