from django.urls import path

from .views import ChatListView, ChatDetailView, ChatCreateView, ChatEditView, ChatDeleteView


urlpatterns = [
    path('chat/<int:pk>/delete', ChatDeleteView.as_view(), name='chat_delete'),
    path('chat/<int:pk>/edit/', ChatEditView.as_view(), name='chat_edit'),
    path('chat/new/', ChatCreateView.as_view(), name='chat_new'),
    path('chat/<int:pk>/', ChatDetailView.as_view(), name='chat_detail'),  # ChatDetailView url expects pk arg to be passed
    path('', ChatListView.as_view(), name='home'),                    # primary key represented as integer by <int:pk>
]