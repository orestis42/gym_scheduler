from django.contrib.auth.backends import BaseBackend
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserRegistrationSerializer
from .models import CustomUser


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        user = get_object_or_404(CustomUser, email=email)
        if password is not None and user.check_password(password):
            return user

class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = EmailBackend().authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_active:
                refresh = RefreshToken.for_user(user)
                response_data = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Account is inactive'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutView(APIView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get('refresh')

        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                if token.token_type != "refresh":
                    raise AuthenticationFailed('Invalid token type.', code='invalid_token_type')
                OutstandingToken.objects.get(token=refresh_token)
                token.blacklist()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except (AuthenticationFailed, TokenError) as e:
                return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            except OutstandingToken.DoesNotExist:
                return Response({'detail': 'Invalid refresh token.'}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'detail': 'Internal server error.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'detail': 'Refresh token not provided.'}, status=status.HTTP_400_BAD_REQUEST)
