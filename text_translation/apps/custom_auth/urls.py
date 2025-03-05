from rest_framework_simplejwt import views
from django.urls import path

urlpatterns = [
    path('login/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
]