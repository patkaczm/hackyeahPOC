from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_api.Serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from chat_bot.models import *
from django.http import HttpResponse, JsonResponse
import json
from chat_bot import engine

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    authentication_classes = (JWTAuthentication,)


    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (AllowAny,)
    authentication_classes = (JWTAuthentication,)

    def create(self, request):
        question = request.data['content']
        print(request.data)
        msg=engine.get_response(question)
        return JsonResponse({'response':msg})


class ConsultantViewSet(viewsets.ModelViewSet):
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer
    permission_classes = (AllowAny,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        queryset = Consultant.objects.all()
        return queryset


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConsultantSerializer
    permission_classes = (AllowAny,)
    authentication_classes = (JWTAuthentication,)

    def list(self, request):
        res_id = 0
        try:
            consultant = Consultant.objects.filter(isAvailable=True)
            if len(consultant):
                conv = Conversation(consultant=consultant[0])
                conv.save()
                res_id = conv.id
            else:
                res_id = -1
            return JsonResponse({'conversation_id': res_id})
        except:
            res_id = -1
            return JsonResponse({'error':'Could not get conversation'})


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = ConsultantSerializer
    permission_classes = (AllowAny,)
    authentication_classes = (JWTAuthentication,)

    def create(self, request):
        req = request.data
        conversation_id = req['conversation_id']
        msg_content = req['message_content']
        try:
            conversation = Conversation.objects.get(id=conversation_id)
            new_message = Message(conversation=conversation, content=msg_content)
            new_message.save()
            print("Conversation finished!")
            return JsonResponse({'result':'Message added successfully'})
        except:
            return JsonResponse({'error':'Could not add the message'})