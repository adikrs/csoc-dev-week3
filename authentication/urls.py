from django.urls import path
#from authentication.views import *
from store.views import *

urlpatterns = [

    #path('^register/$',registerView, name = "register"),
    #path('^login/$',loginView, name = "login"),
    path('',index,name="index"),

    path('^login/$',loginiew, name = "login"),
    path('^logout/$',logoutView, name = "logout"),

]