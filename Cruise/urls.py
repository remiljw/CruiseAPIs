from django.urls import path
from rest_framework_simplejwt import views 

from .apiviews import *

app_name = 'Cruise'



urlpatterns = [
    path('login/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
    path('excursionlist/', ExcursionList.as_view(), name='list'),
]

