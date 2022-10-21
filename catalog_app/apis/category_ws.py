from django.shortcuts import render
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import CreateModelMixin
from django.http import HttpResponse, JsonResponse
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime
from django.db import transaction
from django.db.models import F
from django.core import exceptions
from django.core import mail, serializers
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.permissions import IsAuthenticated

from user_app.models.account_model import Profile
from ..serializers.category_serializer import CategorySerializer, CategoryAddSerializer
from ..models.category_model import Category


# Create your views here.
@permission_classes([IsAuthenticated])
def GetCategoryInfo(request):
    user = request.user
    print(user.username)
    # Get Category info from database # Category.objects.all()
    category_obj = Category.objects.filter(user_id=user.id, active=True).order_by(F('created_at').desc(nulls_last=True))
    # Using Serializer to convert data
    # Set many=True to serializer queryset or list of objects instead of a single object instance
    category_serializer = CategorySerializer(category_obj, many=True)
    return Response(category_serializer.data)


@permission_classes([IsAuthenticated])
def QuerySet_GetCategoryInfo(request):
    user = request.user
    # Get Category info from database # Category.objects.all()
    category_info = Category.objects.filter(user_id=user.id, active=True).order_by(F('created_at').desc(nulls_last=True))
    return category_info


@transaction.atomic()
@permission_classes([IsAuthenticated])
def AddCategory(request):
    print('________vao 12 add AddCategory')
    # Get data from post request
    data = request.data
    user = request.user
    print(data)
    # data['user'] = user.id
    # print(data['product_map'])
    # use Serializer to deserialize data
    serializer = CategoryAddSerializer(data=data)
    print(serializer)
    # Check if validation is successful
    if serializer.is_valid():
        # Save the data to database # serializer.save()
        try:
            category_save = serializer.save()
            # instance = Middleship(
            #     product_id=data['product_map'],
            #     category_id=category_save.id
            #     # date_joined=datetime.now
            # )
            # instance.save()
            # pass
        except exceptions as e:
            print(e.code)
            return Response(e.code, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def json_modelAPI(value_object):
    SomeModel_json = serializers.serialize("json", value_object)
    data = {"SomeModel_json": SomeModel_json}
    return JsonResponse(data)
