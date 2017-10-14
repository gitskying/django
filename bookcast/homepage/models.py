from django.db import models

# Create your models here.

class  FirstPage(models.Model):
    utitle = models.CharField(max_length=20)
    pub_date = models.DateField()
    def __str__(self):
        return '%d' %self.pk