# api/views.py
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from todos import models
from . import serializers

class ListTodo(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('month',)


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
    