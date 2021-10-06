from re import search
from rest_framework import serializers
from register.models import Manager, User, Client, Company


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'company_id']
    



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'cpf', 'email', 'document']



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'cnpj', 'email', 'address', 'city']


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['company_id']