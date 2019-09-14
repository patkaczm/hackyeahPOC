from django.urls import include
from django.conf.urls import url
from rest_framework import routers
from rest_api.ViewSets import *
from django.urls import re_path, path

app_name = 'rest_api'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'consultants', ConsultantViewSet)
router.register(r'conversations', ConversationViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]