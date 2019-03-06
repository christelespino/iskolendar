#This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2015-2016
'''
02/05/2019
	Patrick Joseph Sanchez
		added the EventDetailView and EventCreateView classes, and the maincalendar function
02/06/2019
	Christel Anne Espino	
		added the EventUpdateView and EventDeleteView classes	
02/17/19
	Patrick Joseph Sanchez
		added and implemented the loginrequired decorator, LoginRequiredMixin and UserPassesTestMixin
02/21/19
	Christel Anne Espino
		added daily_view		
'''

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.models import User
from datetime import datetime
from .models import Event, Announcement


context = {
	'events' : Event.objects.all().order_by('date_start'),
	'org' : False
}

# @login_required
def maincalendar(request):
	context = {
		'events' : Event.objects.all().order_by('date_start'),
		'org' : request.user.is_staff
	}
	return render(request, 'maincalendar/maincalendar.html', context)

def daily_view(request):
	try:
		day = datetime.strptime(request.GET.get('date'), '%b. %d, %Y')
	except ValueError:
		day = datetime.strptime(request.GET.get('date'), '%B %d, %Y')
	return render(request, 'maincalendar/daily_view.html', {'event_list': Event.objects.filter(date_start=day).order_by('time_start')})

class EventDetailView(DetailView):
	model = Event

class EventCreateView(LoginRequiredMixin, CreateView):
	model = Event
	fields = ['title', 'description', 'date_start', 'date_end', 'time_start', 'time_end', 'event_type', 'venue', 'scope', 'limit']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Event
	fields = ['title', 'description', 'date_start', 'date_end', 'time_start', 'time_end', 'event_type', 'venue', 'scope', 'limit']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		event = self.get_object()
		if self.request.user == event.author:
			return True
		else:
			return False

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Event
	success_url = '/'

	def test_func(self):
		event = self.get_object()
		if self.request.user == event.author:
			return True
		else:
			return False
#____________________________________________________________________
class AnnouncementCreateView(LoginRequiredMixin, CreateView):
	model = Announcement
	fields = ['event', 'body']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class AnnouncementUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Announcement
	fields = ['body']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		announcement = self.get_object()
		if self.request.user == announcement.author:
			return True
		else:
			return False

class AnnouncementDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Announcement
	success_url = '/'

	def test_func(self):
		announcement = self.get_object()
		if self.request.user == announcement.author:
			return True
		else:
			return False