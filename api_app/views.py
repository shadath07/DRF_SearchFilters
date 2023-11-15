from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends =[SearchFilter]
    # search_fields = ['name','city']
    # search_fields = ['city']
    # This symbols are used to search the name with specific conditions as '^' to search using starting letter of the word.
    search_fields = ['^name']
