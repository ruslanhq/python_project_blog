"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from webapp.views import IndexView, ArticleView, article_create_view, article_update_view, article_delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('article/<int:pk>/', ArticleView.as_view(), name='article_view'),
    path('article/add/', article_create_view, name='article_add'),
    path('article/edit/<int:pk>/', article_update_view, name='article_update'),
    path('article/delete/<int:pk>/', article_delete_view, name='article_delete'),
]