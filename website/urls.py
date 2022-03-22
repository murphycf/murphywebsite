from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('projects/', views.projects, name='projects'),
    path('about/', views.about, name='about'),
    path('uhoh/', views.uhoh, name='uhoh'),
    path('www.github.com/murphycf', views.github, name='github'),
    
]
