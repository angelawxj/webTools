# todos/models.py
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    month = models.TextField(default="0")
    name = models.TextField(default="0")
    incomeChannel = models.TextField(default="0")
    incomeAmount = models.TextField(default="0")
    incomeDate = models.TextField(default="0")
    debtChannel = models.TextField(default="0")
    debtAmount = models.TextField(default="0")
    repayDate = models.TextField(default="0")
    isRepay = models.TextField(default="0")

    def __str__(self):
        """A string representation of the model."""
        return self.title