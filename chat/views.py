# from django.shortcuts import render
# from .models import *
# from .serializers import *
# from rest_framework import permissions
# # Create your views here.
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import generics, status, views
# from django.contrib.auth import authenticate, login

# class AccountRegisterView(generics.GenericAPIView):
#     serializer_class = RegisterSerializer

#     # user create
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'success': True, 'message': 'User created successfully.'},
#                         status=status.HTTP_201_CREATED)


# class LoginView(generics.GenericAPIView):
#     serializer_class = LoginSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)




# class ChatView(APIView):
#     # permission_classes = [permissions.IsAuthenticated]
#     def get(self, request):
#         chats = Chat.objects.all()
#         serializer = ChatSerializer(chats, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         message = request.data.get('message')
#         sender = request.user
#         admin = User.objects.get(is_admin=True)
#         chat = Chat.objects.create(sender=sender, receiver=admin, message=message)
#         serializer = ChatSerializer(chat)
#         return Response(serializer.data)


from rest_framework import generics
from .models import User, Chat
from .serializers import UserSerializer, ChatSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ChatListCreateView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class ChatRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
