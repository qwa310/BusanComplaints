"""complaintPrj URL Configuration

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
from main import views 


urlpatterns = [
    path('', views.index, name="index"),
    path('index2/', views.index2,name = "index2"),
    path('input/', views.complaint_input,name = "input"),
    path('inputform/', views.complaint_input_form,name = "inputform"),
    path('admin/', admin.site.urls),
    # path('students/', include('students.urls')),
    # students라는 url오면 include통해 main앱 내부의 url참조해라
]   