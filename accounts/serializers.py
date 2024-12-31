from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    phoneNumber = serializers.CharField(max_length=15, required=True)
    role = serializers.CharField(max_length=50, required=False, default='User')
    permissions = serializers.ListField(
        child=serializers.CharField(max_length=50),
        required=False,
        default=list,
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password2', 'phoneNumber', 'role', 'permissions')
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        phone_number = self.validated_data['phoneNumber']
        role = self.validated_data.get('role', 'User')
        permissions = self.validated_data.get('permissions', [])

        if password != password2:
            raise serializers.ValidationError({'error': 'Passwords do not match'})
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already exists'})

        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        profile = Profile.objects.create(
            user=account,
            phoneNumber=phone_number,
            role=role,
            permissions=permissions
        )

        return account
