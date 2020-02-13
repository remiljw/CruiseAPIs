from django.urls import path
from rest_framework import routers
from rest_framework.authtoken import views

from .apiviews import *

app_name = 'Cruise'

# router = routers.DefaultRouter()
# router.register('Cruise')

urlpatterns = [
    path('login/', views.obtain_auth_token, name='login'),
    path('users/', UserCreate.as_view(), name="user_create"),
    path('excursionlist/', ExcursionList.as_view(), name='list'),
    path('list/', PollList.as_view(), name='lists')
]

# urlpatterns += router.urls