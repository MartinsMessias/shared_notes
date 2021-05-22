from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from src.register import views as register_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_views.register, name='register'),
    path('', include('django.contrib.auth.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
