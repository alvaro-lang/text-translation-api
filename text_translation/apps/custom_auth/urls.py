from django.urls import path
from rest_framework_simplejwt import views
from .views.UserView import register

urlpatterns = [
    path('login/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', register, name='register'),
]