"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.registration.views import RegisterView
from accounts.views import CustomRegisterView, CustomLoginView  # 추가
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path("accounts/", include('accounts.urls')),
    # path('accounts/', include('dj_rest_auth.urls')),  # 로그인 및 로그아웃 URL
    path('mainpage/', include('mainpage.urls')),
    path('bookmark/', include('bookmark.urls')),  # 북마크 관련 URL
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
