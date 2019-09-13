from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="rest_api:user-detail")
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
