"""hiretutor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from hireapp.views import hireapp, guardian, tutor
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hireapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/guardian/', guardian.GuardianSignUpView.as_view(), name='guardian_signup'),
    path('accounts/signup/tutor/', tutor.TutorSignUpView.as_view(), name='tutor_signup'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)