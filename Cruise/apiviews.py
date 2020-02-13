from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate

from .models import *
from .serializers import *

class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"})

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class ExcursionList(APIView):
    def get(self, request):
        excursion = Excursion.objects.all()
        data = ExcursionSerializer(excursion, many=True).data
        return Response(data)


class PollList(generics.ListCreateAPIView):
    queryset = Excursion.objects.all()
    serializer_class = ExcursionSerializer