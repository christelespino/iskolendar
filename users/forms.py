#This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2015-2016
'''
02/17/19
	Patrick Joseph Sanchez
		extended the form for registration
02/21/19
	Allure Tanquintic
		added fields for registration		
'''

from django import forms
from django.forms import TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class UserRegisterForm(UserCreationForm):
# 	degprogram = [
# 		("1", "Chemical Engineering"),
# 		("2", "Civil Engineering"),
# 		("3", "Computer Science"),
# 		("4", "Computer Engineering"),
# 		("5", "Electrical Engineering"),
# 		("6", "Electronics Engineering"),
# 		("7", "Geodetic Engineering"),
# 		("8", "Industrial Engineering"),
# 		("9", "Mechanical Engineering"),
# 		("10", "Mining Engineering"),
# 		("11", "Metallurgical Engineering"),
# 		("12", "Materials Engineering")
# 	]
	
# 	student_number = forms.CharField(max_length = 9, widget=TextInput(attrs={'type':'number', 'placeholder': '20xxxxxxx'}))
# 	name = forms.CharField(max_length=50)
# 	degree_program = forms.ChoiceField(choices=degprogram, label="Degree Program")
# 	year_standing = forms.IntegerField(max_value = 10)
# 	email = forms.EmailField()

# 	class Meta:
# 		model = User
# 		fields = ['student_number', 'username', 'password1', 'password2', 'name', 'degree_program', 'year_standing', 'email']

##################################################################################################################################
class UserRegisterForm(UserCreationForm):
	degprogram = [
		("1", "Chemical Engineering"),
		("2", "Civil Engineering"),
		("3", "Computer Science"),
		("4", "Computer Engineering"),
		("5", "Electrical Engineering"),
		("6", "Electronics Engineering"),
		("7", "Geodetic Engineering"),
		("8", "Industrial Engineering"),
		("9", "Mechanical Engineering"),
		("10", "Mining Engineering"),
		("11", "Metallurgical Engineering"),
		("12", "Materials Engineering")
	]
	
	student_number = forms.CharField(max_length = 9, widget=TextInput(attrs={'type':'number', 'placeholder': '20xxxxxxx'}))
	name = forms.CharField(max_length=50)
	position = forms.CharField(max_length=100)
	organization = forms.CharField(max_length=100)
	org_acronym = forms.CharField(max_length=20)
	degree_program = forms.ChoiceField(choices=degprogram, label="Degree Program")
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['student_number', 'username', 'password1', 'password2', 'name', 'position', 'organization', 'org_acronym', 'degree_program', 'email', 'is_staff']	