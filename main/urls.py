from django.urls import path

from main.views import AnnouncementListAPIView, AnnouncementCreteAPIView, AnnouncementUpdateDeleteAPIView, GetDistricts, \
    GetRegions, GetBlogs, DeleteAnnouncement, BlogCreate, BlogUpdateDelete

urlpatterns = [
    path('announcement-list', AnnouncementListAPIView.as_view(), name='announcement_list'),
    path('announcement', AnnouncementCreteAPIView.as_view(), name='announcement'),
    path('announcement-upd/<int:pk>', AnnouncementUpdateDeleteAPIView.as_view(), name='announcement_update_delete'),
    path('get-regions', GetRegions.as_view(), name='get_regions'),
    path('get-district', GetDistricts.as_view(), name='get_districts'),
    path('blogs', GetBlogs.as_view(), name='blogs'),
    path('blog-create', BlogCreate.as_view(), name='blog_create'),
    path('blog-update-delete/<int:pk>', BlogUpdateDelete.as_view(), name='blog_update_delete'),

    path('delete-announcement/<int:pk>', DeleteAnnouncement.as_view(), name='delete_announcement')
]
