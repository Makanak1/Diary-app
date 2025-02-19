from rest_framework.views import APIView
from rest_framework import status,serializers
from rest_framework.response import Response

from .serializers import DiarySerializer
from . models import Diary

from django.contrib.auth import authenticate, login, logout

# Create your views here.
class DiaryView(APIView):
    def get(self, request):
        try:
            entries = Diary.objects.all()
            serializer = DiarySerializer(entries, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = DiarySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DiaryDetailView(APIView):
    def get(self, request, id):
        try:
            entry = Diary.objects.get(id=id)
            serializer = DiarySerializer(entry)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Diary.DoesNotExist:
            return Response({"error": "Diary entry not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        try:
            entry = Diary.objects.get(id=id)
            serializer = DiarySerializer(instance=entry, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Diary.DoesNotExist:
            return Response({"error": "Diary entry not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id):
        try:
            entry = Diary.objects.get(id=id)
            entry.delete()
            return Response({"message": "Diary entry deleted successfully"}, status=status.HTTP_200_OK)
        except Diary.DoesNotExist:
            return Response({"error": "Diary entry not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RegisterUserView(APIView):
    def post(self,request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginUserView(APIView):
    def post(self,request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return Response({'message': 'Login successful'},status=status.HTTP_200_OK)
            return Response({'error': 'username or password'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LogoutUserView(APIView):
    def post(self,request):
        try:
            logout(request)
            return Response({'message': 'Logout successful'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)