from rest_framework import fields, serializers
from enroll.models import User

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']