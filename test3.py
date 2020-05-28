@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ExcursionDetail(request):
    excursion = Excursion.objects.all()
    data = ExcursionSerializer(excursion, many=True).data
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ExcursionList(request, id):
    try:
        excursion = Excursion.objects.get(id=id)
    except:
        Excursion.DoesNotExist 
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ExcursionSerializer(excursion)
        return Response(serializer.data)
      

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateExcursion(request):
    serializer = ExcursionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def EditExcursion(request, id):
        try:
            excursion = Excursion.objects.get(id=id)
        except: 
            Excursion.DoesNotExist 
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = ExcursionSerializer(excursion)
            return Response(serializer.data)
        elif request.method == 'PATCH':
            serializer = ExcursionSerializer(excursion, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

