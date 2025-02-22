from users.apps import UserConfig
from rest_framework.routers import DefaultRouter
from rest_framework.permissions import AllowAny
from users.views import UserViewSet, PaymentListAPIView, PaymentCreateAPIView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = UserConfig.name
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
urlpatterns = [
    path('payment/', PaymentListAPIView.as_view(), name='payment'),
    path('token/', TokenObtainPairView.as_view(permission_classes=[AllowAny]), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=[AllowAny]), name='token_refresh'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
] + router.urls
