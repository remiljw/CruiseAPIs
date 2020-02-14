from rest_framework import  status,generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Excursion
from .serializers import ExcursionSerializer

class ExcursionLists(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Excursion.objects.raw('SELECT * FROM cruise_excursion')
    serializer_class = ExcursionSerializer
    def lists(self, request):
        queryset = self.get_queryset
        serializer = ExcursionSerializer(queryset, many=True)
        return Response(serializer.data)

  

class SingleExcursion(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Excursion.objects.all()
    serializer_class = ExcursionSerializer

      

class CreateExcursion(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExcursionSerializer
    def post(self, request):
        serializer = ExcursionSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
class EditExcursion(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Excursion.objects.all()
    serializer_class = ExcursionSerializer
  
 
        




        


