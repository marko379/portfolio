from django.shortcuts import render
# from django.db.models import Q
# from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from django.http import HttpResponse
from .models import Projects
from .serializers import Project_Serializer
# from django.http import JsonResponse
# from rest_framework.renderers import JSONRenderer
# import json


class all_projects(APIView):

    def get(self, request, format=None):
        projects = Projects.objects.all()
        serializer = Project_Serializer(projects, many=True)
        return Response(serializer.data)

class project(APIView):
    def get(self, request, slug):
        get_project = Projects.objects.get(slug=slug)
        serializer = Project_Serializer(get_project)
        return Response(serializer.data)

