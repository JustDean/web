"""ask URL Configuration

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
from django.urls import path, include
# from django.contrib.auth import login, logout # doesn't work wounder why

import qa.views as views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainView.as_view(), name='main'),
    # path('login/', login, {'template_name': 'login.html'}, name='login'),
    # path('signup/', views.test, name='signup'),
    path('question/', include('qa.urls'), name='questions'),
    path('ask/', views.ask_question, name='ask'),
    path('popular/', views.PopularView.as_view(), name='popular'),
    # path('new/', views.NewQuestion.as_view(), name='new'),
]
