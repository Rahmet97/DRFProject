from django.urls import path

from main.views import AnnouncementAPIView

urlpatterns = [
    path('get-announcement', AnnouncementAPIView.as_view(), name='get_announcement')
]
