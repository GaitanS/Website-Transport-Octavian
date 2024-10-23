"""
URL configuration for OctavianLogistic1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from main.views import homepage, send_email

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # URL for language switching
]

# Localized URL patterns (these will have language prefixes like /en/ or /ro/)
urlpatterns += i18n_patterns(
    path('', homepage, name='homepage'),  # Homepage with language prefix
    path('send_email/', send_email, name='send_email'),
    path('admin/', admin.site.urls),
)
