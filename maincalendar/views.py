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