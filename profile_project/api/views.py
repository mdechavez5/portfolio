from django.shortcuts import render
from rest_framework import generics, status
from .serializers import ProjectSerializer
from .models import Project

# Create your views here.

class ProjectListView(generics.ListAPIView):
    model = Project
    serializer_class = ProjectSerializer