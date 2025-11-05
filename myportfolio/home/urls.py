from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', include('contact.urls')),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),   # add trailing slash
]