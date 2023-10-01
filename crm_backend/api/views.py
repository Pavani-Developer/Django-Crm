from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.permissions import IsAdminUser,DjangoModelPermissions
from rest_framework import generics
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView





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

@api_view(['GET'])
def getDev(request):
    data = Enrol.objects.filter(course = 'devops')
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
    #data = StudentJoin.objects.all()
    student = JoinSerializer(data = request.data)
    name = request.data["name"]
    username = request.data["username"]
    password = request.data["password"]
    email = request.data["email"]
    #We are creating user for student to acccess studentdash board
    user = User.objects.create_user(username, email, password)
    user.save()
    to_list = [email]
    send_mail(
            name,
            """
            Hi {},\n Welcome to our Website.\n Your Username is :{}\n Password:{} """.format(name,username,password),
            settings.EMAIL_HOST_USER,
            to_list
            
        )
    if student.is_valid():
        student.save()
        return Response(student.data,status = status.HTTP_201_CREATED)
    else:
        return Response("Invalid Data",status = status.HTTP_400_BAD_REQUEST )

#This API function for getting students from joined data

@api_view(['GET'])
def getjoin(request):
    data = StudentJoin.objects.all()
    s_data = JoinSerializer(data,many = True)

    return Response(s_data.data)

#This API function for getting single student from joined data

@api_view(['GET'])
def getjoinData(request,pk):
    data = StudentJoin.objects.get(id = pk)
    s_data = JoinSerializer(data)

    return Response(s_data.data)

#Function for posting contact data to the Backend

@api_view(['POST'])
def contactData(request):
    details = ContactSerializer(data = request.data)
    #print(student)
    if details.is_valid():
        details.save()
        return Response(details.data,status = status.HTTP_201_CREATED)
    else:
        return Response("Invalid Data",status = status.HTTP_400_BAD_REQUEST )

#Function for posting demo data to the Backend
@api_view(['POST'])
def demoData(request):
    demo = DemoSerializer(data=request.data)
    print(demo)
    if demo.is_valid():
        demo.save()
        return Response(demo.data,status = status.HTTP_201_CREATED)
    else:
        return Response("Invalid Data",status = status.HTTP_400_BAD_REQUEST )

#Function for returning demo data to the frontend
@api_view(['GET'])
def getdemoData(request):
    data = Demo.objects.all()
    s_data = DemoSerializer(data,many = True)

    return Response(s_data.data)


@api_view(['POST'])
def userLogin(request):
    data = UserSerializer(data=request.data)
    username = request.data["username"]
    password = request.data["password"]
    try:
        user = authenticate(request.data,username=username,password=password)
        if user.is_active and not user.is_staff:
            print(user.is_valid())
            return Response(True,status=status.HTTP_202_ACCEPTED)
        else:
            print("no")
            return Response(None,status=status.HTTP_401_UNAUTHORIZED)
    except:
        return Response(True,status=status.HTTP_202_ACCEPTED)

        
@api_view(['GET'])
def getUser(request):
    data = User.objects.all()
    s_data = UserSerializer(data,many = True)

    return Response(s_data.data)

@api_view(['POST'])
def adminLogin(request):
    permission_classes = (IsAuthenticated, )
    data = UserSerializer(data=request.data)
    username = request.data["username"]
    password = request.data["password"]
    try:
        user = authenticate(request.data,username=username,password=password)
        if user.is_staff and not user.is_superuser:
            
            return Response(True,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(None,status=status.HTTP_401_UNAUTHORIZED)
    except:
        return Response(True,status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def superLogin(request):
    data = UserSerializer(data=request.data)
    username = request.data["username"]
    password = request.data["password"]
    try:
        user = authenticate(request.data,username=username,password=password)
        if user.is_superuser:
            
            return Response(True,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(None,status=status.HTTP_401_UNAUTHORIZED)
    except:
        return Response(True,status=status.HTTP_202_ACCEPTED)


class LogoutView(APIView):
     permission_classes = (IsAuthenticated,)
     def post(self, request):
          
          try:
               refresh_token = request.data["refresh_token"]
               token = RefreshToken(refresh_token)
               token.blacklist()
               return Response(status=status.HTTP_205_RESET_CONTENT)
          except Exception as e:
               return Response(status=status.HTTP_400_BAD_REQUEST)




