from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('home/',views.home,name='Home-home'),
    path('about/',views.about,name="Home-about"),
    path('contact/',views.contactus,name='Home-contactus'),
    path('forgotpassword/', views.forgotpassword, name='Home-forgotpassword'),
    path('login/',views.login,name='Home-login'),
    path('register/',views.Register,name='Home-Register'),
    path('checklogin/',views.checklogin,name='checklogin'),
    path('addregister/',views.addregister,name='register'),
    path('contactsave/',views.contactsave,name='Home-contact'),
    path('base2/',views.base2,name='Home-base'),
    path('logout/', views.logout, name='logout'),

]