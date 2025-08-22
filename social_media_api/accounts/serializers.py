from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()  # ensures we use the custom User model

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "bio", "profile_picture", "token"]

    def create(self, validated_data):
        # Create user using get_user_model().objects.create_user
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            password=validated_data["password"],
            bio=validated_data.get("bio", ""),
            profile_picture=validated_data.get("profile_picture", None),
        )
        # Create a token for the new user
        token = Token.objects.create(user=user)
        user.token = token.key  # temporary for serializer output
        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["token"] = Token.objects.get(user=instance).key
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

