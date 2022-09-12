from django.urls import path

from .views import getUser

urlpatterns = [
    path('get-user', getUser, name='get_user')
]
