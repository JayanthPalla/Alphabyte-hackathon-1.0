from django.urls import path
from .views import RecruiterUserRegisterAPIView, RecruiterUserLoginAPIView

urlpatterns = [
    path('register/', RecruiterUserRegisterAPIView.as_view(), name='rec_user_register'),
    path('login/', RecruiterUserLoginAPIView.as_view(), name='rec_user_login'),
]
