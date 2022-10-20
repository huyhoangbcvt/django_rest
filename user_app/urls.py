from django.urls import path, include
from .modules import views_auth, form_auth
from rest_framework import viewsets
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.views import (
    LoginView, LogoutView,
)
app_name = 'user'

user_list = views_auth.UserViewSet.as_view({
    'get': 'list',
    # 'post': 'create'
})
profile_list = views_auth.ProfileViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
group_list = views_auth.GroupViewSet.as_view({
    'get': 'list',
})
token_user = TokenObtainPairView.as_view()
token_refresh = TokenRefreshView.as_view()
# register = views_auth.register

# urlpatterns = format_suffix_patterns([
#     path('users/', user_list, name='user_list'),
#     path('profiles/', profile_list, name='user_list'),
#     path('groups/', group_list, name='user_list'),
#     path('get-token/', token_user, name='token_obtain_pair'),
#     # Để cấp mới access token với refresh token, ta thực hiện POST request
#     path('refresh-token/', token_refresh, name='token_refresh'),
#     path('sign-up/', register, name='sign_up'),
# ])

# If using routers to register ViewSet, it will see Binding ViewSets to urls explicitly
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', views_auth.UserViewSet, basename="user_list")
router.register(r'profiles', views_auth.ProfileViewSet, basename="profile_list")
router.register(r'groups', views_auth.GroupViewSet, basename="user_group_list")
# router.register(r'users/<int:pk>', views_auth.UserDetail, basename="user_detail")

# If not register ViewSet, it only to see urls detail
urlpatterns = [
    # path('<int:pk>/', views_auth.UserDetail.as_view()),
    # path('', views_auth.index, name='index'),
    path('', include(router.urls)),
    # path('users/', user_list, name='user_list'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # djoser endpoints: Django REST framework # Create account in jwt
    # path('auth/', include('djoser.urls')),  # Create account: /user/auth/users/
    # get access & refresh token in jwt
    # path('auth/', include('djoser.urls.jwt')),  # Login auth Headers: /user/auth/jwt/create/
    path('get-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Để cấp mới access token với refresh token, ta thực hiện POST request
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sign-up/', views_auth.register, name='sign_up'),
    # path("login/", views_auth.CustomAuthToken.as_view(), name="login"),
    # # path('accounts/login/', views_auth.LoginView.as_view(), name="login_view_api"),
    # path('accounts/login/', LoginView.as_view(
    #             form_class=form_auth.LoginForm,
    #             template_name='login.html',
    #             extra_context={'next': '/'},
    #             success_url='/',
    #     ), name="login_view_api"),
]
