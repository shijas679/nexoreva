# config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Core dashboard (home/landing)
    path('', include('dashboard.urls')),

    # Staff management
    path('staff/', include('staff.urls')),

    # Course management
    path('courses/', include('course.urls')),  # ✅ Added properly
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
