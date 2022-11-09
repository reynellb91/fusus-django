from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import User, Organization


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'phone', 'email', 'birthdate', 'organization')


class OrganizationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"


class GroupModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)