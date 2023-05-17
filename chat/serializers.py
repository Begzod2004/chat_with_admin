# from django.contrib.auth import authenticate
# from django.contrib.auth.hashers import check_password
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.utils.encoding import force_str
# from django.utils.http import urlsafe_base64_decode
# from rest_framework import serializers
# from rest_framework.exceptions import AuthenticationFailed
# # from home.serializers import StudentSerializer
# from .models import User


# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(min_length=6, max_length=68, write_only=True)
#     password2 = serializers.CharField(min_length=6, max_length=68, write_only=True)

#     class Meta:
#         model = User
#         fields = ('id', 'user_type','phone_number','chats_received','chats_sent', 'full_name', 'username', 'password', 'password2',)
#         # fields = ('user_type','full_name','username','date_of_birth','gender','objects','groups','password', 'password2')
#     def validate(self, attrs):
#         password = attrs.get('password')
#         password2 = attrs.get('password2')

#         if password != password2:
#             raise serializers.ValidationError({'success': False, 'message': 'Password did not match, please try again'})
#         return attrs

#     def create(self, validated_data):
#         del validated_data['password2']
#         return User.objects.create_user(**validated_data)



# from rest_framework import serializers
# from .models import *
# # class UserSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = User
# #         fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
# #         extra_kwargs = {'password': {'write_only': True}}


# class ChatSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Chat
#         fields = ['sender', 'receiver', 'message', 'created_at']


# class LoginSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(max_length=100, required=True)
#     password = serializers.CharField(max_length=68, write_only=True)
#     user_type = serializers.CharField(read_only=True)
#     tokens = serializers.SerializerMethodField(read_only=True)

#     def get_tokens(self, obj):
#         username = obj.get('username')
#         tokens = User.objects.get(username=username).tokens
#         return tokens

#     class Meta:
#         model = User
#         fields = ('username', 'user_type', 'tokens', 'password')

#     def validate(self, attrs):
#         username = attrs.get('username')
#         password = attrs.get('password')
#         user = authenticate(username=username, password=password)
#         if not user:
#             raise AuthenticationFailed({
#                 'message': 'username or password is not correct'
#             })
#         if not user.is_active:
#             raise AuthenticationFailed({
#                 'message': 'Account disabled'
#             })

#         data = {
#             'username': user.username,
#             'user_type': user.user_type,
#         }
#         return data





from rest_framework import serializers
from .models import User, Chat


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_type', 'phone_number', 'full_name', 'username']


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'sender', 'receiver', 'message', 'created_at']
