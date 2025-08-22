from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

from .serializers import RegisterSerializer, LoginSerializer, UserSerializer

User = get_user_model()


# --------------------------
# Registration endpoint
# --------------------------
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    # create() method is handled by serializer
    # Returns user data + token automatically


# --------------------------
# Login endpoint
# --------------------------
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        # Get or create token
        token, _ = Token.objects.get_or_create(user=user)

        # Return token + serialized user
        return Response({
            "token": token.key,
            "user": UserSerializer(user).data
        })


# --------------------------
# Profile endpoint (get/update)
# --------------------------
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Only allow access to own profile
        return self.request.user

