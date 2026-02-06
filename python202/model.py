from django.db import  models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.enums()
    city = models.CharField(max_length=20)
    

from rest_framework import serializers


class StudentsSerilizer(serializers.Serializer):
    name = models.CharField(max_length=100)
    age = models.enums()
    city = models.CharField(max_length=20)
    
class   StudentsSerilizer(serializers.ModelSerializer):
       class meta :
           models = Student
           fields = ["name" ,"roll_num" ,"city"]
           
           
           
           
           