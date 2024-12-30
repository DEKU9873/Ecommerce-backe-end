from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . views import registeation_view, logout_view, change_user_role, get_all_users


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', registeation_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('users/', get_all_users, name='users'),
    path('role/<int:user_id>/', change_user_role, name='role'),
]