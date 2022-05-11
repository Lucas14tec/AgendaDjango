
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from Questions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('eventos/<int:evento_id>' , views.evento),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
