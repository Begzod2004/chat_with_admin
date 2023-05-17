from django.urls import path
from .views import *
urlpatterns = [
    # path('chat/', ChatView.as_view(), name='chat'),
    # path('register/', AccountRegisterView.as_view()),
    # path('login/', LoginView.as_view()),
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('chats/', ChatListCreateView.as_view(), name='chat-list'),
    path('chats/<int:pk>/', ChatRetrieveUpdateDestroyView.as_view(), name='chat-detail'),
]

# from django.urls import path
# from .views import UserListCreateView, UserRetrieveUpdateDestroyView, ChatListCreateView, ChatRetrieveUpdateDestroyView

# urlpatterns = [
#     path('users/', UserListCreateView.as_view(), name='user-list'),
#     path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
#     path('chats/', ChatListCreateView.as_view(), name='chat-list'),
#     path('chats/<int:pk>/', ChatRetrieveUpdateDestroyView.as_view(), name='chat-detail'),
# ]

