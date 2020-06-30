from rest_framework import serializers
from django.contrib.auth import get_user_model

class MyUserSerializer(serializers.ModelSerializer):

      class Meta:
          model = get_user_model()
          exclude = ('password', 'user_permissions', 'groups')