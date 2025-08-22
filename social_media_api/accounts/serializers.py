from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "bio", "profile_picture", "token"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(**validated_data, password=password)
        token, _ = Token.objects.get_or_create(user=user)
        user.token = token.key  # temporary attribute for serializer output
        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        token = Token.objects.get(user=instance)
        data["token"] = token.key
        return data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Invalid username or password")
        data["user"] = user
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "bio", "profile_picture"]

