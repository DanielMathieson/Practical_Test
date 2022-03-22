"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.urls import include
from ga_courses import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.course, name="course"),
    path('ga_courses/', include('ga_courses.urls')),
    # The above maps any URLs starting with ga_courses/ to be handled by ga_courses.
    path('admin/', admin.site.urls),
]

