from django.urls import path
from rest_framework_simplejwt import views 

from .apiviews import *

app_name = 'Cruise'



urlpatterns = [
    path('api/login/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/excursion/details/', ExcursionDetail.as_view(), name='details'),
    path('api/excursion/<int:pk>/', ExcursionList.as_view(), name='list'),
    path('api/excursion/create/', CreateExcursion.as_view(), name='create')
]

