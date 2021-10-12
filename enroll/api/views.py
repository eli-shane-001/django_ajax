from enroll.models import User
from enroll.api.serializers import Userserializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class userview(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]