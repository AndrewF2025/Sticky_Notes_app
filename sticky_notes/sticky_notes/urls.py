"""
URL configuration for sticky_notes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# sticky_notes/sticky_notes/urls.py
from django.contrib import admin
from django.urls import path, include

# Define the URL patterns for the project
urlpatterns = [
    # Admin site URL
    path("admin/", admin.site.urls),

    # Include the URLs from the notes app
    path("", include("notes.urls")),
]
