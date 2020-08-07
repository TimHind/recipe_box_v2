"""recipe_box URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from recipe_app.views import recipe_view, author_view, main_view, recipe_detail, author_detail

urlpatterns = [
    path('', main_view),
    path('recipe/<int:recipe_id>/', recipe_detail),
    path('authors/<int:author_id>/', author_detail),
    path('authors/', author_view),
    path('recipe/', recipe_view),
    path('admin/', admin.site.urls),
]
