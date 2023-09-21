from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.permissions import IsAdminUser,DjangoModelPermissions
from rest_framework import generics


# Create your views here
# .
@api_view(['GET'])
def getData(request):
    data = Enrol.objects.all()
    s_data = EnrolSerializer(data,many=True)
    return Response(s_data.data)


#Function for returning only python data to the react
@api_view(['GET'])
def getPython(request):
    data = Enrol.objects.filter(course = 'python')
    s_data = EnrolSerializer(data,many=True)
    return Response(s_data.data)

#Function for returning only java data to the react
@api_view(['GET'])
def getJava(request):
    data = Enrol.objects.filter(course = 'java')
    s_data = EnrolSerializer(data,many=True)
    return Response(s_data.data)

#Function for returning only Testing data to the react

@api_view(['GET'])
def getTesting(request):
    data = Enrol.objects.filter(course = 'testing')
    s_data = EnrolSerializer(data,many=True)
    return Response(s_data.data)

#Funtion for posting Enrol data
@api_view(['POST'])
def insertData(request):
    student = EnrolSerializer(data = request.data)
    #print(student)
    if student.is_valid():
        student.save()
        return Response(student.data,status = status.HTTP_201_CREATED)
    else:
        return Response("Invalid Data",status = status.HTTP_400_BAD_REQUEST )

#Function for posting joined data
@api_view(['POST'])
def insertjoinData(request):
    student = JoinSerializer(data = request.data)
    print(student)
    if student.is_valid():
        student.save()

        
        return Response(student.data,status = status.HTTP_201_CREATED)
    else:
        return Response("Invalid Data",status = status.HTTP_400_BAD_REQUEST )

#This API function for getting single student from joined data
@api_view(['GET'])
def getjoin(request):
    data = StudentJoin.objects.all()
    s_data = JoinSerializer(data,many = True)

    return Response(s_data.data)
@api_view(['GET'])
def getjoinData(request,pk):
    data = StudentJoin.objects.get(id = pk)
    s_data = JoinSerializer(data)

    return Response(s_data.data)

@api_view(['POST'])
def contactData(request):
    details = ContactSerializer(data = request.data)
    #print(student)
    if details.is_valid():
        details.save()
        return Response(details.data,status = status.HTTP_201_CREATED)
    else:
        return Response("Invalid Data",status = status.HTTP_400_BAD_REQUEST )

@api_view(['POST'])
def demoData(request):
    demo = DemoSerializer(data=request.data)
    print(demo)
    if demo.is_valid():
        demo.save()
        return Response(demo.data,status = status.HTTP_201_CREATED)
    else:
        return Response("Invalid Data",status = status.HTTP_400_BAD_REQUEST )

@api_view(['GET'])
def getdemoData(request):
    data = Demo.objects.all()
    s_data = DemoSerializer(data,many = True)

    return Response(s_data.data)



