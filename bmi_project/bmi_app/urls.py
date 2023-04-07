from django.urls import path
from bmi_app.views import calculate_bmi

urlpatterns = [
    path('', calculate_bmi, name='calculate_bmi'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)