from django.contrib import admin
from django.conf.urls import path,include

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include('blog.urls')),
]
