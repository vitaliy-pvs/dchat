import os

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Message, Settings
from .serializers import MessageSerializer
from chatsite.settings import STATIC_ROOT


STATIC_ROOT = STATIC_ROOT.replace("\\", "/")


favicon_exists = False
if os.path.isfile(os.path.join(STATIC_ROOT, 'favicon.png')):
    favicon_exists = True

logo_exists = False
if os.path.isfile(os.path.join(STATIC_ROOT, 'logo.png')):
    logo_exists = True

header_img_exists = False
if os.path.isfile(os.path.join(STATIC_ROOT, 'header.jpg')):
    header_img_exists = True


settings = Settings.objects.all()


def room(request):
    return render(request, 'base.html', {
        'settings': settings[0],
        'favicon_exists': favicon_exists,
        'logo_exists': logo_exists,
        'header_img_exists': header_img_exists,
    })


class MessageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response({"messages": serializer.data})

    def post(self, request):
        message = request.data.get('message')
        serializer = MessageSerializer(data=message)
        if serializer.is_valid(raise_exception=True):
            message_saved = serializer.save()
            messages_count = Message.objects.all().count()
            messages_count_to_del = messages_count - 100
            if messages_count_to_del > 0:
                messages_arr = Message.objects.all().order_by('pk')
                for number in range(messages_count_to_del - 1):
                    Message.objects.filter(pk=messages_arr[number].pk).delete()

        return Response({"success": "Message from '{}' saved successfully".format(message_saved.username)})
