# api/views.py
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from . import serializers
from . import models

class ListReport(generics.ListCreateAPIView):
    queryset = models.Report.objects.all()
    serializer_class = serializers.ReportSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('month',)


class DetailReport(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Report.objects.all()
    serializer_class = serializers.ReportSerializer

class ListInterview(generics.ListCreateAPIView):
    queryset = models.Interview.objects.all()
    serializer_class = serializers.InterviewSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('sort','fatherSort',)


class DetailInterview(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Interview.objects.all()
    serializer_class = serializers.InterviewSerializer