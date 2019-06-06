# todos/models.py
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    month = models.TextField(default="-")
    name = models.TextField(default="-")
    incomeChannel = models.TextField(default="-")
    incomeAmount = models.TextField(default="-")
    incomeDate = models.TextField(default="-")
    debtChannel = models.TextField(default="-")
    debtAmount = models.TextField(default="-")
    repayDate = models.TextField(default="-")
    isRepay = models.TextField(default="-")

    def __str__(self):
        """A string representation of the model."""
        return self.title