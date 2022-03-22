from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('projects.html', include('website.urls')),
    path('uhoh.html', include('website.urls')),
    
]