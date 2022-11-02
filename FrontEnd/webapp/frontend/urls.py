from django.urls import path

from . import views
# Controladores
#from controllers import userController

urlpatterns = [
    path('', views.home, name = 'home'),
    path('login', views.login_view, name = 'login_view'),
    # Administration
    path('users', views.users, name = 'users'),
    path('setting', views.setting, name = 'setting'),
    path('resources', views.resources, name = 'resources'),
]