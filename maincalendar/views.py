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
03/06/2019
	Patrick Joseph Sanchez
    	added views for announcements
03/15/2019
	Christel Anne Espino
		fixed announcements display on main calendar    	
03/20/2019
	Patrick Joseph Sanchez
    	added addparticipant function
03/21/2019
	Patrick Joseph Sanchez
    	added addparticipant function
03/21/2019
	Christel Anne Espino
		added personal_calendar function  
		added error message for addparticipant  	
'''

from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Event, Announcement
from users.models import Profile
from .announcement_form import AnnouncementForm
import datetime


context = {
	'events' : Event.objects.all().order_by('date_start'),
	'org' : False,
	'announcements' : Announcement.objects.all().order_by('date_posted'),
	'id'  : 0,
	'date' : datetime.date.today(),
}

# @login_required
def maincalendar(request):
	curr_date = datetime.date.today()
	start_week = curr_date - datetime.timedelta(curr_date.weekday())
	end_week = start_week + datetime.timedelta(7)
	context = {
		'events' : Event.objects.all().order_by('date_start'),
		'org' : request.user.is_staff,
		'announcements' : Announcement.objects.filter(date_posted__range=[start_week, end_week]),
		'id'  : request.user.pk,
		'date' : datetime.date.today(),
	}
	return render(request, 'maincalendar/maincalendar.html', context)

def daily_view(request):
	try:
		day = datetime.datetime.strptime(request.GET.get('date'), '%b. %d, %Y')
	except ValueError:
		day = datetime.datetime.strptime(request.GET.get('date'), '%B %d, %Y')
	return render(request, 'maincalendar/daily_view.html', {'event_list': Event.objects.filter(date_start=day).order_by('time_start')})	

def announcements_view(request):
	return render(request, 'maincalendar/announcement_view.html', {'announcement_list': Announcement.objects.all().order_by('date_posted')})

def addparticipant(request):
	event_add = Event.objects.filter(pk=request.GET.get('event')).first()
	num = event_add.limit
	userprof = Profile.objects.filter(user = request.user)[0]

	if num == event_add.participants.all().count():
		messages.error(request, 'Event has reached its limit.')
	elif event_add.deg_prog != "N/A" and event_add.deg_prog != userprof.degree_program:
		messages.error(request, 'Degree program not part of the scope.')
	else:	
		event_add.participants.add(request.user)

	return redirect('event-detail', pk = request.GET.get('event'))

def removeparticipant(request):
	event_remove = Event.objects.filter(pk=request.GET.get('event')).first()
	event_remove.participants.remove(request.user)
	return redirect('event-detail', pk = request.GET.get('event'))

def personal_calendar(request):
	if request.user.is_authenticated:
		context = {
			'events' : request.user.events_joined.all().order_by('date_start'),
			'logged' : request.user.is_authenticated
		}
	else:
		context = {
			'events' : None,
			'logged' : request.user.is_authenticated
		}	
	return render(request, 'maincalendar/personal_calendar.html', context)

class EventDetailView(DetailView):
	model = Event

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['user_joined'] = False

		for s in context['object'].participants.all():
			if s == self.request.user:
				context['user_joined'] = True
				break
		return context

class EventCreateView(LoginRequiredMixin, CreateView):
	model = Event
	fields = ['title', 'description', 'date_start', 'date_end', 'time_start', 'time_end', 'event_type', 'venue', 'deg_prog', 'limit']
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
	template_name = 'maincalendar/announcement_form.html'
	form_class = AnnouncementForm

	def get_form_kwargs(self):
		kwargs = super(AnnouncementCreateView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs

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