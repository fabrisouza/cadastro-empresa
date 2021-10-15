from rest_framework import viewsets
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Client, Company, User
from .serializers import (ClientSerializer, CompanySerializer, ListSerializer,
                          UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            "user": str(request.user),
            "auth": str(request.auth),
        }
        return Response(content)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            "user": str(request.user),
            "auth": str(request.auth),
        }
        return Response(content)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            "user": str(request.user),
            "auth": str(request.auth),
        }
        return Response(content)


#class ManagerViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = ManagerSerializer
#    authentication_classes = [SessionAuthentication, BasicAuthentication]
#    permission_classes = [IsAuthenticated]
#
#    def get(self, request, format=None):
#        content = {
#            "user": str(request.user),
#            "auth": str(request.auth),
#        }
#        return Response(content)
#
#    def get_queryset(self):
#        return super().get_queryset().filter(type="Manager")


class ListViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ListSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            "user": str(request.user),
            "auth": str(request.auth),
        }
        return Response(content)
