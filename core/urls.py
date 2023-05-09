from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from page.views import *


urlpatterns = [
    #account
    path('admin/', admin.site.urls),
    #page
    path('', index,name='home'),
    path('about/', about,name='about'),
    path('mission/', about,name='mission'),
    path('vision/', about,name='vision'),
    path('contact/', contact,name='contact'),
    path('produck/', produck,name='produck'),
    path('meeting/', meeting,name='meeting'),
    path('announcement/', announcement,name='announcement'),
    path("single_produck/<int:id>/",single_produck,name="single_produck"),
    path("single_announcement/<int:id>/",single_announcement,name="single_announcement"),

]
urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)