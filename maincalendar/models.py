#This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2015-2016

'''
02/05/2019
Patrick Joseph Sanchez
	added the Event class
02/06/2019
Christel Anne Espino	
	added choices for event type and scope, modified the Event model
'''

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


EVENT_TYPE = (
	('seminar', 'SEMINAR'),
	('workshop', 'WORKSHOP'),
	('convention', 'CONVENTION'),
	('review session', 'REVIEW SESSION'),
	('applicants\' orientation', 'APPLICANTS\' ORIENTATION'),
	('competition', 'COMPETITION'),
	('outreach', 'OUTREACH'),
	('fundraising', 'FUNDRAISING'),
	('others', 'OTHERS'),
)

SCOPE_CHOICES = (
	('program-restricted', 'PROGRAM-RESTRICTED'),
	('college-restricted', 'COLLEGE-RESTRICTED'),
	('university-wide', 'UNIVERSITY-WIDE'),
	('open to all', 'OPEN TO ALL'),
)

class Event(models.Model):
	title = models.CharField(max_length = 100)
	description = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)
	date_start = models.DateField(default = timezone.now)
	date_end = models.DateField(default = timezone.now)
	time_start = models.TimeField(default=None, blank=True, null=True)
	time_end = models.TimeField(default=None, blank=True, null=True)
	event_type = models.CharField(max_length = 100, default=None, blank=True, null=True, choices=EVENT_TYPE)
	venue = models.CharField(max_length = 500, default=None, blank=True, null=True)
	scope = models.CharField(max_length = 50, default=None, blank=True, null=True, choices=SCOPE_CHOICES)
	limit = models.IntegerField(default=None, blank=True, null=True)
	#author = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('event-detail', kwargs = {'pk': self.pk})
