from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Announcement
from .serializers import AnnouncementSerializer


class AnnouncementAPIView(APIView):
    authentication_classes = []

    def get(self, request):
        try:
            ann = Announcement.objects.all()
            announcement_list = AnnouncementSerializer(ann, many=True).data
        except:
            announcement_list = None
        return Response(announcement_list)
