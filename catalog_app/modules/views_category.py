from datetime import datetime
from django.shortcuts import render, resolve_url, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import login, logout
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.decorators import api_view, action, permission_classes, authentication_classes, renderer_classes
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.renderers import JSONRenderer
# from django_filter import FilterSet
from ..apis import category_ws
from ..serializers.category_serializer import CategorySerializer
from ..models.category_model import Category
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET'])
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
# @renderer_classes([JSONRenderer])
def GetCategoryInfo(request):
    return category_ws.GetCategoryInfo(request)


@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Basic Auth
# @authentication_classes([TokenAuthentication])
@csrf_exempt
def AddCategory(request):
    print('________________________________vao 11 add AddCategory')
    return category_ws.AddCategory(request)


class CategoryInfoViewSet(viewsets.ModelViewSet):
    # authentication_classes = TokenAuthentication  # Token access
    permission_classes = [IsAuthenticated]  # Basic Auth
    queryset = Category.objects.filter(active=True).order_by('created_at')
    serializer_class = CategorySerializer
    charset = 'UTF-8'

    @action(methods=['POST'], detail=True)
    def add(self, request):
        print(request)
        # return category_ws.AddCategory(request)
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        # price_lte = request.GET['price_lte']
        print(self.request.user)


class CreateCategory(CreateModelMixin, GenericAPIView):
    serializer_class = CategorySerializer
    # authentication_classes = TokenAuthentication  # Token access
    permission_classes = [IsAuthenticated]          # Basic Auth

    def post(self, request, *args, **kwargs):
        print(self.request.data)
        print(self.request.data.get("user"))
        return self.create(request, *args, **kwargs)
        # return HttpResponse('ok POST')

    # def perform_create(self, serializer):
    #    _id = self.request.data.get('id')
    #    comment = get_object_or_404(Profile, pk=_id)
    #    print(comment)


# Get all
# class ListAllProfile(ListAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = User_appSerializer
#     permission_classes = [IsAuthenticated]


# class CreateProfile(CreateModelMixin, GenericAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request, *args, **kwargs):
#         # print(self.request.data)
#         # print(self.request.data.get("name"))
#         return self.create(request, *args, **kwargs)
#
#     # def perform_create(self, serializer):
#     #    _id = self.request.data.get('id')
#     #    comment = get_object_or_404(Profile, pk=_id)
#     #    print(comment)