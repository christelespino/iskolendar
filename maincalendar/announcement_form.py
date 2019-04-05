#This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2015-2016
'''
03/06/19
	Patrick Joseph Sanchez
		extended the form for announcement
'''

from django import forms
from django.forms import TextInput
from django.contrib.auth.models import User
from .models import Event, Announcement
class AnnouncementForm(forms.ModelForm):
	class Meta:
		model = Announcement
		fields = ['event', 'subject', 'body']

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user')
		super(AnnouncementForm, self).__init__(*args, **kwargs)
		self.fields['event'].queryset = Event.objects.filter(author=user)