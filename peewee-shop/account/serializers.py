from dataclasses import fields
import imp
from pyexpat import model
from abstract.serializers import BaseSerializer
from .models import MyUser

class UserSerializer(BaseSerializer):
    class Meta:
        fields = ("id", "username")
        model = MyUser