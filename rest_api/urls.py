from django.urls import include
from django.conf.urls import url
from rest_framework import routers
from rest_api.ViewSets import UserViewSet
from django.urls import re_path, path

app_name = 'rest_api'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'hello/', UserViewSet.as_view(), name='hello'),
    path('hello/', UserViewSet.as_view({'get':'list'}), name='hello'),
]

curl 127.0.0.1:8000/api/users/ -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY4MzkxODA1LCJqdGkiOiI4M2QyNGZiYTc1Njk0YzY4OWQ0MDZmYzg3NjA1NDc1OSIsInVzZXJfaWQiOjF9.SduSPSXr_czbzE0x85uuOIQDlm5REVmzmwkWxJYBI_4'
