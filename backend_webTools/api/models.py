from django.db import models

# Create your models here.
class Report(models.Model):
    title = models.CharField(max_length=200)
    month = models.TextField(default="-")
    name = models.TextField(default="-")
    incomeChannel = models.TextField(default="-")
    incomeAmount = models.TextField(default="-")
    incomeDate = models.TextField(default="-")
    debtName = models.TextField(default="-")
    debtChannel = models.TextField(default="-")
    debtAmount = models.TextField(default="-")
    repayDate = models.TextField(default="-")
    isRepay = models.TextField(default="-")
    numDebt = models.TextField(default="-")
    debtType = models.TextField(default="-")

    def __str__(self):
        """A string representation of the model."""
        return self.title

class Interview(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField(default="-")
    star = models.TextField(default="-")
    ispass = models.TextField(default="-")
    sort = models.TextField(default="-")
    fatherSort = models.TextField(default="-")

    def __str__(self):
        """A string representation of the model."""
        return self.question