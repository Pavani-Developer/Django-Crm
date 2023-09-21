from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User




class EnrolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrol
        fields = '__all__'

class JoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentJoin
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class DemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demo
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['username','password']
