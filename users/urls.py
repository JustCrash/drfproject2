from users.apps import UserConfig
from rest_framework.routers import DefaultRouter
from rest_framework.permissions import AllowAny
from users.views import UserViewSet, PaymentListAPIView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = UserConfig.name
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
urlpatterns = [
    path('payment/', PaymentListAPIView.as_view(), name='payment'),
    path('api/token/', TokenObtainPairView.as_view(permission_classes=[AllowAny]), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(permission_classes=[AllowAny]), name='token_refresh'),
] + router.urls
