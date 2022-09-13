from django.contrib.auth.models import User
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import UserSerializer


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def getUser(request):
    try:
        users = request.user
        users_json = UserSerializer(users)
        data = {
            'data': users_json.data
        }
    except Exception as e:
        data = {
            'error': f'{e}'
        }
    return Response(data)
