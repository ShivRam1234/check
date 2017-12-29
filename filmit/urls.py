from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve
from filmitouch.views import HomeView, BlogDetailView, search_status, mobi_search, ContactView1

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^', include('filmitouch.urls'), name='filmitouch'),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^blog/(?P<slug>[-\w]+)/*$', BlogDetailView.as_view(), name='blog-detail'),
    url(r'^search_status/$', search_status, name='search'),
    url(r'^search_status1/$', mobi_search, name='search_mobile'),
    url(r'^contact/$', ContactView1.as_view(), name='contact'),
]
if settings.DEBUG:
    urlpatterns += [
                       url(r'^static/(?P<path>.*)$', serve)
                   ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# serving media files only on debug mode
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]
