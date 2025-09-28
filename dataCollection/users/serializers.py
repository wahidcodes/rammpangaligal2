from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ExtraInfo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]
        extra_kwargs = {"password":{"write_only":True}}

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email already exists.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class ExtraInfoSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = ExtraInfo
        fields = ["id", "username", "phone_no", "address", "created_at"]