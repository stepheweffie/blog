from django.conf.urls import url
from django.contrib import admin
from django_app import views
from django.conf.urls.static import static
import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.post_list, name='post_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, documentroot=settings.STATIC_ROOT)