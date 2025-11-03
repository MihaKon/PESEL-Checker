from django.contrib import admin
from django.urls import path
from core.views import PeselCheckView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", PeselCheckView.as_view(), name="check"),
]
