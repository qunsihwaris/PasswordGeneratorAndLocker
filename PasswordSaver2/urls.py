"""PasswordSaver2 URL Configuration

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
from frontend.views import home, Register, LogIn
from deshboard.views import deshboard, signout, passgen, add, show

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register', Register, name='register_page'),
    path('login', LogIn, name='login_page'),
    path('deshboard', deshboard, name='deshboard_page'),
    path('signout', signout, name='signout_page'),
    path('passwordgenerator', passgen, name='passgen_page'),
    path('additem', add, name='add_page'),
    path('show', show, name='show_page')
]
