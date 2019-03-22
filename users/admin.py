#This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2015-2016
'''
03/22/2019
	Patrick Joseph Sanchez
		made the Profiles visible in the admin page
'''
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
# Register your models here.
