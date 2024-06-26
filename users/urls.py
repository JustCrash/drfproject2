from users.apps import UserConfig
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, PaymentListAPIView
from django.urls import path


app_name = UserConfig.name
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
urlpatterns = [
    path('payment/', PaymentListAPIView.as_view(), name='payment')
] + router.urls
