from django.db import models


class Medicine(models.Model):

    class Meta:
        db_table = "medicine"

    name    = models.CharField(verbose_name="医薬品名",max_length=100)

    def __str__(self):
        return self.name




