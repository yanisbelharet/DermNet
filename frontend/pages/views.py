from django.shortcuts import render

def login_view(request):
    return render(request, 'auth/login.html')

def patient_dashboard(request):
    return render(request, 'patient/dashboard.html')

def patient_scans(request):
    return render(request, 'patient/scans.html')

def patient_prescriptions(request):
    return render(request, 'patient/prescriptions.html')

def patient_support(request):
    return render(request, 'patient/support.html')

def dermatologue_dashboard(request):
    return render(request, 'dermatologue/dashboard.html')

def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')
