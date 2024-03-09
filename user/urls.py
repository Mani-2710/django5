from django.urls import path
from .import views
urlpatterns=[
    path('',views.horoscopes,name='horoscopes'),
    path('horoscopes/',views.horoscopes,name='user-horoscopes'),
    path('daily/',views.daily,name='user-daily'),
    path('weekly/',views.weekly,name='user-weekly'),
    path('monthly/',views.monthly,name='user-monthly'),
    path('yearly/',views.yearly,name='user-yearly'),
    path('service/',views.service,name='user-service'),
    path('reading/',views.reading,name='user-reading'),
    path('chartanalysis/',views.chartanalysis,name='user-chartanalysis'),
    path('save_horoscope/', views.save_horoscope, name='save-horoscope'),
]