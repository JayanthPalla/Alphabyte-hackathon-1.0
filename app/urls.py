from django.urls import path
from .views import ApplicantUserRegisterAPIView, ApplicantUserLoginAPIView

urlpatterns = [
    path('register/', ApplicantUserRegisterAPIView.as_view(), name='app_user_register'),
    path('login/', ApplicantUserLoginAPIView.as_view(), name='app_user_login'),
]
