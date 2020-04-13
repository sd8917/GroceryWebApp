from django.db import models

# Create your models here.
# Create your models here.
class Customer_Detail(models.Model):
    name = models.CharField(max_length=55)
    number = models.BigIntegerField()
    product = models.CharField(max_length=20)
    place = models.CharField(max_length=20)

    def __str__(self):
        return self.name + '  -   ' + str(self.number)