from pydoc import doc
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializer
# Create your views here.


from .models import Doctor

@api_view(['GET'])
def addUser(request):
    doctor = Doctor.objects.all()
    print(doctor)
    serializer = ItemSerializer(doctor,many=True)
    print(serializer)
    return Response(serializer.data)


@api_view(['POST'])
def addUser(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)