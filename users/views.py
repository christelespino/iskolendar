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
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, "Account created!")

			student_number = form.cleaned_data.get('student_number')
			name = form.cleaned_data.get('name')
			position = form.cleaned_data.get('position')
			organization = form.cleaned_data.get('organization')
			org_acronym = form.cleaned_data.get('org_acronym')
			degree_program = form.cleaned_data.get('degree_program')
			
			profile = Profile()
			profile.student_number = student_number
			profile.name = name
			profile.position = position
			profile.organization = organization
			profile.org_acronym = org_acronym
			profile.degree_program = degree_program
			profile.user = User.objects.filter(username = username)[0]
			profile.save()

			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})
