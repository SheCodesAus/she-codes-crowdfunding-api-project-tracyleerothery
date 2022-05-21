# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status, generics, permissions

# from crowdfunding.projects import permissions, serializers
# from .models import CustomUser
# from .serializers import CustomUserSerializer, RegisterSerializer

# from pickletools import read_stringnl_noescape_pair
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer, RegisterSerializer, CustomUserDetailSerializer

# View a list of ALL user profiles on the website
class CustomUserList(APIView):
    def get(self, request):
          users = CustomUser.objects.all()
          serializer = CustomUserSerializer(users, many=True)
          return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
        return Response(serializer.errors)

# User Profile View
class CustomUserDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly
        ]

    def get_object(self, username):
          try:
               return CustomUser.objects.get(username=username)
          except CustomUser.DoesNotExist:
               raise Http404

    def get(self, request, username):
        user = self.get_object(username)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        data = request.data
        serializer = CustomUserDetailSerializer(
            instance=user,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# "Creating user account view" == Register Account

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permissions_clsasses = [permissions.AllowAny,]
    queryset = CustomUser.objects.all()

# class BadgeView(generics.ListCreateAPIView):
#     serializer_class = BadgeSerializer
#     queryset = Badge.objects.all()
#     permission_classes = [permissions.IsAdminUser]   