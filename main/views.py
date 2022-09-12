from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer


@api_view(['GET'])
def getUser(request):
    try:
        users = User.objects.filter(is_superuser=False)
        users_json = UserSerializer(users.data, many=True)
        data = {
            'data': users_json
        }
    except Exception as e:
        data = {
            'error': f'{e}'
        }
    return Response(data)
