from django.contrib.auth.models import User, Group
from api.models import User, Company
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    employees = serializers.StringRelatedField(many=True)
    class Meta:
        model = Company
        fields = ['company', 'employees']

