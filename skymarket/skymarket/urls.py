from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
    path("api/", include('ads.urls')),
    path("api/", include('users.urls')),
    path("api/token/", TokenObtainPairView.as_view(), name='token'),
    path("refresh/", TokenRefreshView.as_view(), name='refresh-token'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
