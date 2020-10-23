from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from students.models import Student
from students.serializers import StudentModelSerializer
# Create your views here.
class StuentAPIView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
