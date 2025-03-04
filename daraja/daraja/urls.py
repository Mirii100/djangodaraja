
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('personal.urls')),  # Add this line
    path('admin/', admin.site.urls),
]
