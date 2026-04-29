from django.urls import path
from . import views

urlpatterns = [
    path('',                         views.login_view,             name='home'),
    path('auth/login/',              views.login_view,             name='login'),
    path('patient/dashboard/',       views.patient_dashboard,      name='patient_dashboard'),
    path('patient/scans/',           views.patient_scans,          name='patient_scans'),
    path('patient/prescriptions/',   views.patient_prescriptions,  name='patient_prescriptions'),
    path('patient/support/',         views.patient_support,        name='patient_support'),
    path('dermatologue/dashboard/',  views.dermatologue_dashboard, name='dermatologue_dashboard'),
    path('admin-panel/dashboard/',   views.admin_dashboard,        name='admin_dashboard'),
]