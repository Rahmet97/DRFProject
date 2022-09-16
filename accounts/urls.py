from django.urls import path


from .views import getUser, login, register

urlpatterns = [
    # path('<username>', getUser, name='user'),
    path('login', login, name='login'),
    path('register', register, name='register')
]
