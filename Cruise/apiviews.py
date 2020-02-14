from rest_framework import  status,generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


from .models import Excursion
from .serializers import ExcursionSerializer

class ExcursionLists(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Excursion.objects.raw('SELECT * FROM cruise_excursion')
    serializer_class = ExcursionSerializer
    def detail(self, request):
        queryset = self.get_queryset
        serializer = ExcursionSerializer(queryset, many=True)
        return Response(serializer.data)

  

class SingleExcursion(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        excursion = get_object_or_404(Excursion, id=id)
        data = ExcursionSerializer(excursion).data
        return Response(data)
      

class CreateExcursion(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExcursionSerializer

class EditExcursion(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Excursion.objects.all()
    serializer_class = ExcursionSerializer
  
 
        




        


