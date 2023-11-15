from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import * 
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

# @api_view(['GET','POST','PUT','DELETE','PATCH'])
# def studentapi(request):
#     if request.method == 'GET':
#         id = request.data.get('id')
#         if id is not None:
#             stu = Student.objects.get(id = id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many = True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'masg':'Data Created'})
#         return Response(serializer.errors)
    
#     if request.method == 'PUT':
#         id = request.data.get('id')
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data = request.data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':"Data Updated!"})
#         return Response(serializer.errors)
    
#     if request.method == 'DELETE':
#         id = request.data.get('id')
#         stu = Student.objects.get(pk =id) 
#         stu.delete()
#         return Response({'msg':'Data Deleted Successfully!'})
            

# This is for the browser based api view ------> some changes with respest to getting the id using pk 

# @api_view(['GET','POST','PUT','DELETE','PATCH'])
# def studentapi(request, pk = None):
#     if request.method == 'GET':
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id = id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many = True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'masg':'Data Created'},status = status.HTTP_201_CREATED)
#         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'PUT':
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':"complete Data Updated!"})
#         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'PATCH':
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data = request.data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':"Partial Data Updated!"})
#         return Response(serializer.errors)
    
#     if request.method == 'DELETE':
#         id = pk
#         stu = Student.objects.get(pk =id) 
#         stu.delete()
#         return Response({'msg':'Data Deleted Successfully!'})
    
# Class Based Views ------------------>

class StudentAPI(APIView):
    def get(self,request,pk=None,format = None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)
    
    def post(self,request,format = None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'masg':'Data Created'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,format = None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"complete Data Updated!"})
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def Patch(self,request,  pk,format = None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Partial Data Updated!"})
        return Response(serializer.errors)
    
    def delete(self,request,pk,format = None):
        id = pk
        stu = Student.objects.get(pk =id) 
        stu.delete()
        return Response({'msg':'Data Deleted Successfully!'})