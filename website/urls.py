from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from music import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    #add music url since django starts to check this on request
    url(r'^music/', include('music.urls')),
    #add video url since django starts to check this on request
    url(r'^videos/', include('videos.urls')),
    #add gallery url since django starts to check this on request
    path('',include('gallery.urls')),
    #my first trial of restframework
    url(r'ngoma/', views.AlbumList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)