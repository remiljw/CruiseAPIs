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
        if data.is_valid():
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(data, status=status.HTTP_404_NOT_FOUND)

class ExcursionList(APIView):
    def get(self, request, pk):
        excursion = get_object_or_404(Excursion, pk=pk)
        data = ExcursionSerializer(excursion).data
        if data.is_valid:
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(data, status=status.HTTP_404_NOT_FOUND)



class CreateExcursion(APIView):
    serializer_class = ExcursionSerializer

    def post(self, request):
        data = {''
        
        }
        serializer = ExcursionSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class EditExcursion(APIView):
#     serializer_class = ExcursionSerializer

#     def put(self, request, pk)


