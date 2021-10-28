from django.contrib import admin
from django.urls import path
from django.urls.conf import include

# from rest_framework_jwt.views import obtain_jwt_token , refresh_jwt_token, verify_jwt_token
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView,)

urlpatterns = [
    # path('login/', obtain_jwt_token),
    # path('refresh-token/', refresh_jwt_token),
    # path('verify-token/', verify_jwt_token),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
]