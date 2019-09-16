from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import BlacklistMixin


class UserAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def delete(self, request, format=None):
        # simply delete the token to force a login
        token_base64 = request.META.get('HTTP_AUTHORIZATION').split()[1]

        toke = BlacklistMixin.for_user(request.user)


        return Response(toke, status=status.HTTP_200_OK)
