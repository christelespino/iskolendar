#This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2015-2016

'''
02/17/19
	Patrick Joseph Sanchez
		created the register function w/c creates a form and checks the validity of the input of the user
'''


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from .models import Profile


def register(request):
	if request.method == 'POST':
		print("hi")
		form = UserRegisterForm(request.POST)
		print(form.errors)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, "Account created!")
			
			profile = Profile()
			profile.student_number = form.cleaned_data.get('student_number')
			profile.name = form.cleaned_data.get('name')
			profile.position = form.cleaned_data.get('position')
			profile.organization = form.cleaned_data.get('organization')
			profile.org_acronym = form.cleaned_data.get('org_acronym')
			profile.college = form.cleaned_data.get('college')
			profile.degree_program = form.cleaned_data.get('degree_program')
			profile.user = User.objects.filter(username = username)[0]
			profile.save()

			print("hey")
			return redirect('login')
	else:
		form = UserRegisterForm()
		print("hello")
	return render(request, 'users/register.html', {'form': form})
