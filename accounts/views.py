from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import LoginValidateSerializer, SignupValidateSerializer


@api_view(['POST'])
def signup_api_view(request):
    serializer = SignupValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    validated_data = serializer.validated_data
    validated_data['is_active'] = False
    user = User.objects.create_user(**serializer.validated_data)
    return Response(data={'message': 'User created', 'user_id': user.id})



@api_view(['POST'])
def login_api_view(request):
    #1
    serializer = LoginValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    #2
    user = authenticate(**serializer.validated_data)

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={'message': 'Successfull authorization',
                              'key': token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED,
                    data={'message': 'Unauthorized'})

    #3


