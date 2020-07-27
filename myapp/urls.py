from . import views
from django.urls import path
from django.contrib.auth import views as auth_views 

urlpatterns = [    
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('secure/', views.secure, name='secure'), 
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    url('account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
]   
]

from django.conf.urls import url
from mysite.core import views as core_views

