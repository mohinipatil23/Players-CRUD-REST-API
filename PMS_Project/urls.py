
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playersapi/', include('playersrecordapp.urls')),  # Include URLs from playersrecordapp
]
