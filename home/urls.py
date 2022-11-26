from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('signup1/', views.signup1, name = 'signup1'),
    path('signup1/signup2/', views.signup2, name = 'signup2'),
    path('signup1/signup2/login/', views.login, name = 'login'),
    path('home/', views.home, name = 'home'),

    # path('home/doctor/', views.redirectTo, name = 'home'),
    path('doctor/', views.doctorPage, name = 'doctorPage'),
    path('about/', views.about, name = 'about'),
    path('services/', views.services, name = 'services'),
    path('appointment/', views.appointment, name = 'appointment')


    # path('login/home/', views.redirectToHome, name = 'redirectToHome')
    

    # path('signup1/signup2/login/home/', views.home, name = 'home'),
    # path('signup2/home/', views.home, name = 'home'),
    # path('signup2/', views.signup2, name = 'signup2'),
    # path('login/', views.index, name = 'login'),
]