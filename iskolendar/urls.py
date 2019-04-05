#This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2015-2016

'''
02/05/2019
	Patrick Joseph Sanchez
		created the file (added path for admin and maincalendar)
02/17/19
	Patrick Joseph Sanchez
		added path to register page, login and logout page
'''

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    path('', include('maincalendar.urls')),
]