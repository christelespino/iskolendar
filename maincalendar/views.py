#This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2015-2016
'''
02/05/2019
Patrick Joseph Sanchez
	added the EventDetailView and EventCreateView classes, and the maincalendar function
02/06/2019
Christel Anne Espino	
	added the EventUpdateView and EventDeleteView classes	
'''

from django.shortcuts import render
#from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Event


def maincalendar(request):
	context = {
		'events' : Event.objects.all()
	}
	return render(request, 'maincalendar/maincalendar.html', context)

class EventDetailView(DetailView):
	model = Event

class EventCreateView(CreateView):
	model = Event
	fields = ['title', 'description', 'date_start', 'date_end', 'time_start', 'time_end', 'event_type', 'venue', 'scope', 'limit']

class EventUpdateView(UpdateView):
	model = Event
	fields = ['title', 'description', 'date_start', 'date_end', 'time_start', 'time_end', 'event_type', 'venue', 'scope', 'limit']

	def test_func(self):
		event = self.get_object()
		return True

class EventDeleteView(DeleteView):
	model = Event
	success_url = '/'

	def test_func(self):
		event = self.get_object()
		return True