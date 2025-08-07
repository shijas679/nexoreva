# config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Core dashboard (home/landing)
    # path('', include('dashboard.urls')),

    # Staff management
    path('staff/', include('staff.urls')),

    # Course management
    path('courses/', include('course.urls')),  # ✅ Added properly
    path('', include('attendance.urls')),      # << Make attendance home the default page
    path('dashboard/', include('dashboard.urls')),  # << dashboard now at /dashboard/
    path('staff/', include('staff.urls')),
<<<<<<< HEAD
    path('',include('attendance.urls'))

=======
    path('workassignment/', include('workassignment.urls')),  # ✅ keep this line
>>>>>>> 28e399ea911099c4bdee3ba6522c8c812e4f67e4
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
