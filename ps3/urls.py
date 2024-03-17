from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recruiter/', include('rec.urls')),
    path('applicant/', include('app.urls')),
]
