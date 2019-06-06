# api/serializers.py
from rest_framework import serializers
from todos import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'month',
            'name',
            'incomeChannel',
            'incomeAmount',
            'incomeDate',
            'debtChannel',
            'debtAmount',
            'repayDate',
            'isRepay'
        )
        model = models.Todo