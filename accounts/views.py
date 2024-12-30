from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from .models import *


@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    

@api_view(['POST'])
def registeation_view(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            profile = Profile.objects.get(user=account)  

            data['response'] = "Successfully registered a new user"
            data['id'] = account.id
            data['username'] = account.username
            data['email'] = account.email
            data['phoneNumber'] = profile.phoneNumber  
            data['role'] = profile.role
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
            
        return Response({"data": data})   



@api_view(['GET'])
@permission_classes([IsAdminUser])  # السماح فقط للأدمن
def get_all_users(request):
    users = User.objects.all()  # جلب جميع المستخدمين
    data = []

    # المرور على جميع المستخدمين وجمع بياناتهم
    for user in users:
        try:
            profile = Profile.objects.get(user=user)
            user_data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'phoneNumber': profile.phoneNumber,
                'role': profile.role,
            }
            data.append(user_data)
        except Profile.DoesNotExist:
            # في حال عدم وجود الملف الشخصي
            user_data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'phoneNumber': None,
                'role': None,
            }
            data.append(user_data)

    return Response({'users': data})

@api_view(['PUT'])
@permission_classes([IsAdminUser])  
def change_user_role(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'detail': 'User not found'}, status=404)

    # الحصول على البيانات الجديدة من الطلب
    username = request.data.get('username', user.username)
    email = request.data.get('email', user.email)
    phone_number = request.data.get('phoneNumber', user.profile.phoneNumber)
    role = request.data.get('role', user.profile.role)

    # تحديث بيانات المستخدم
    user.username = username
    user.email = email
    user.save()

    # تحديث بيانات الملف الشخصي (Profile)
    profile = user.profile
    profile.phoneNumber = phone_number
    profile.role = role
    profile.save()

    # تغيير الدور
    if role == 'Admin':
        user.is_staff = True
    else:
        user.is_staff = False
    user.save()

    return Response({'detail': 'User account updated successfully'})