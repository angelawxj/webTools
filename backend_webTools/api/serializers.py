# api/serializers.py
from rest_framework import serializers
from . import models


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'month',
            'name',
            'incomeChannel',
            'incomeAmount',
            'incomeDate',
            'debtName',
            'debtChannel',
            'debtAmount',
            'repayDate',
            'isRepay'
        )
        model = models.Report

class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'question',
            'answer',
            'star',
            'ispass',
            'sort',
            'fatherSort',
        )
        model = models.Interview