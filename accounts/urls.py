from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . views import registeation_view


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', registeation_view, name='register'),
]





