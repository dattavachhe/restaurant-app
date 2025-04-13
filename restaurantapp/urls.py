

from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('base',views.base,name='base'),
    path('menu', views.menu, name='menu'),
    path('contact', views.contact, name='contact'),
    path('reserve', views.reserve, name='reserve'),
    path('login_page',views.login_page,name='login_page'),
    path('manual_logout',views.manual_logout,name='manual_logout'),
path('profile',views.profile,name='profile'),

    path('signup',views.signup,name='signup'),
]