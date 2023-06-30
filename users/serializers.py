from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import BaseUserManager
from rest_framework import serializers
from users.models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'name', 'membership_type']
        extra_kwargs = {
            'email': {'validators': []},
            'membership_type': {'required': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def validate(self, data):
        email = BaseUserManager.normalize_email(data['email'])
        if CustomUser.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({"email": "A user with this email already exists."})
        return data
