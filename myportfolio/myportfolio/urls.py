from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),  # ✅ Add 'contact/' prefix
    path('', include('home.urls')),             # ✅ Keep home at root
]