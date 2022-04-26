from django.urls import path
from django.conf.urls import url
from . import views
from .views import *

app_name = 'libraryApp'
urlpatterns = [
    path('create',views.create),
    path('listuser',views.retrieve),
    path('list',views.retrieveAdminList),
    path('update/<str:bookName>',views.update),
    path('delete/<str:bookName>',views.delete),
    path('home',views.home),
    path('signup',admin_sign_up.as_view()),
    url(r'^login/$', views.user_login, name='user_login')
]