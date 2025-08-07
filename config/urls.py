# config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('dashboard.urls')),
    path('staff/', include('staff.urls')), 
    path('certificate/', include('certificate.urls')),

    # Core dashboard (home/landing)
    # path('', include('dashboard.urls')),

    # Staff management
    path('staff/', include('staff.urls')),

    # Course management
    path('courses/', include('course.urls')),  # ✅ Added properly
    path('', include('attendance.urls')),      # << Make attendance home the default page
    path('dashboard/', include('dashboard.urls')),  # << dashboard now at /dashboard/
    path('staff/', include('staff.urls')),
    path('',include('attendance.urls')),

    path('workassignment/', include('workassignment.urls')),  # ✅ keep this line
    path('',include('task_trakking.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
