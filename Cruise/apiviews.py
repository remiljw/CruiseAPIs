from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


from .models import Excursion
from .serializers import ExcursionSerializer


class ExcursionDetail(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        excursion = Excursion.objects.all()
        data = ExcursionSerializer(excursion, many=True).data
        return Response(data, status=status.HTTP_200_OK)

class ExcursionList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, id):
        excursion = get_object_or_404(Excursion, id=id)
        data = ExcursionSerializer(excursion).data
        return Response(data, status=status.HTTP_200_OK)
      



class CreateExcursion(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ExcursionSerializer

    def post(self, request):
        data = {
        
        }
        serializer = ExcursionSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EditExcursion(APIView):
    serializer_class = ExcursionSerializer
    permission_classes = (IsAuthenticated,)

    # def put(self, request, id):
        


