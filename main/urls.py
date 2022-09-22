from django.urls import path

from main.views import AnnouncementListAPIView, AnnouncementCreteAPIView, AnnouncementUpdateDeleteAPIView, GetDistricts, \
    GetRegions, GetBlogs, DeleteAnnouncement

urlpatterns = [
    path('announcement-list', AnnouncementListAPIView.as_view(), name='announcement_list'),
    path('announcement', AnnouncementCreteAPIView.as_view(), name='announcement'),
    path('announcement-upd/<int:pk>', AnnouncementUpdateDeleteAPIView.as_view(), name='announcement_update_delete'),
    path('get-regions', GetRegions.as_view(), name='get_regions'),
    path('get-district', GetDistricts.as_view(), name='get_districts'),
    path('blogs', GetBlogs.as_view(), name='blogs'),
    path('delete-announcement/<int:pk>', DeleteAnnouncement.as_view(), name='delete_announcement')
]
