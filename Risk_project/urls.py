"""Risk_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy

from Risk_project_ufps.core_risk.dto.models import Actividad

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Risk_project_ufps.urls")),
    path('reset/password_reset', 
    	PasswordResetView.as_view(
    		template_name='registration/password_reset_formf.html', 
    		email_template_name='registration/password_reset_emailf.html'), 
    	name="password_reset"
    	),
    path('reset/password_reset_done', 
    	PasswordResetDoneView.as_view(
    		template_name='registration/password_reset_donef.html'), 
    	name = 'password_reset_done'
    	),
    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', 
    	PasswordResetConfirmView.as_view(
    		template_name='registration/password_reset_confirmf.html'), 
    	name = 'password_reset_confirm'
    	),
    path('reset/done',
    	PasswordResetCompleteView.as_view(
    		template_name='registration/password_reset_completef.html'
    	), 
    	name = 'password_reset_complete'
    	),
]







