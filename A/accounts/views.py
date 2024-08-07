from django.contrib.auth import logout
from rest_framework.parsers import MultiPartParser , FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from . import serializers
from . import models
from home import models as home_model
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from permissions import IsOwnerOrReadOnly

# Create your views here.

class UserRegister(APIView):
    serializer_class = serializers.UserRegisterSerializer
    def post(self,req):
        ser_data = serializers.UserRegisterSerializer(data=req.POST)
        if ser_data.is_valid():
            User.objects.create_user(
                username=ser_data.validated_data['username'],
                email=ser_data.validated_data['email'],
                password=ser_data.validated_data['password'],
            )
            return Response("register successful")
        return Response(ser_data.errors)

class UserLogout(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    def get(self,request):
        request.user.auth_token.delete()
        logout(request)
        return Response('logged out')


class UserViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = serializers.UserViewSetSerializer

    def list(self,request):
        ser_data = serializers.UserViewSetSerializer(instance=self.queryset,many=True)
        return Response(data=ser_data.data)

    def retrieve(self,request ,pk=None):
        user = get_object_or_404(self.queryset,pk=pk)
        if user == request.user:
            ser_date = serializers.UserViewSetSerializer(instance=user).data
            return Response(ser_date)
        return Response('not yours')

    def partial_update(self,request,pk=None):
        user = get_object_or_404(self.queryset,pk=pk)
        ser_data = serializers.UserViewSetSerializer(instance=user,data=request.data,partial=True)
        if request.user.id==user.id:
            if ser_data.is_valid():
                ser_data.save()
                return Response(ser_data.data)
            return Response(ser_data.errors)
        return Response("not yours")


    def destroy(self,request,pk=None):
        user = get_object_or_404(self.queryset,pk=pk)
        if user == request.user:
            user.is_active=False
            user.save()
            return Response('user deactivated')
        return Response("not yours")

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        profile = models.Profile.objects.all()
        ser_data = serializers.ProfileViewSetSerializer(instance=profile,many=True).data
        return Response(ser_data,status=status.HTTP_200_OK)

class ProfileCreateView(APIView):
    parser_classes = [MultiPartParser,FormParser]
    authentication_classes = [TokenAuthentication]
    def post(self,request,name):
        user = get_object_or_404(User,username=name)
        ser_data = serializers.ProfileViewSetSerializer(data=request.data,instance=user)
        if ser_data.is_valid():
            ser_data.save()

            return Response(ser_data.data)
        return Response(ser_data.errors)


