from django.shortcuts import render

# Create your views here.
import json

from django.shortcuts import render

# Create your views here.
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import UserSerializer, UserRegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class SignUpView(views.APIView):
    def post(self, request):
        request_data = json.loads(request.body)
        serializer = UserRegistrationSerializer(data=request_data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response(UserSerializer(user).data)


class SignInView(views.APIView):
    def post(self, request):
        request_data = json.loads(request.body)
        email = request_data.get('email', '')
        password = request_data.get('password', '')
        user = authenticate(email=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
