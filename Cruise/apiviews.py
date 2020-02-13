from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


from .models import Excursion
from .serializers import ExcursionSerializer


class ExcursionList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        excursion = Excursion.objects.all()
        data = ExcursionSerializer(excursion, many=True).data
        return Response(data)

