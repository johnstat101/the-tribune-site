from . import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/',include('news.urls'))
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
