
from rest_framework import generics, viewsets
from .serializers import UserSerializer, ClientSerializer, CompanySerializer, ManagerSerializer  
from .models import Client, Company, User, Manager
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]



    def  get(self, request, format = None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]



    def  get(self, request, format = None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]



    def  get(self, request, format = None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]



    def  get(self, request, format = None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)