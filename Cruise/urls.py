from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .apiviews import *

app_name = 'Cruise'




urlpatterns = [
   
    path('api/', include([
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('excursion/lists/', ExcursionLists.as_view(), name='details'),
    path('excursion/<int:id>/', SingleExcursion.as_view(), name='list'),
    path('excursion/create/', CreateExcursion.as_view(), name='create'),
    path('excursion/update/<int:pk>/', EditExcursion.as_view(), name='update'),
    ]))
    
]

