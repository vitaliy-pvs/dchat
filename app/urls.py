from django.urls import path
from .views import MessageView, room

app_name = "messages"
urlpatterns = [
    path('', room, name='room'),
    path('api/messages/', MessageView.as_view()),
]
