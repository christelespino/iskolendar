#This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2015-2016

'''
02/05/2019
	Patrick Joseph Sanchez
		added the Event class
02/06/2019
	Christel Anne Espino	
		added choices for event type and scope, modified the Event model
02/17/2019
	Patrick Joseph Sanchez
		added the author foreign key attribute in Event model
03/06/2019
	Patrick Joseph Sanchez
		added the announcement model
03/20/2019
	Patrick Joseph Sanchez
    	added participants field in event model
'''

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

EVENT_TYPE = (
	('Seminar', 'SEMINAR'),
	('Workshop', 'WORKSHOP'),
	('Convention', 'CONVENTION'),
	('Review Session', 'REVIEW SESSION'),
	('Applicants\' Orientation', 'APPLICANTS\' ORIENTATION'),
	('Competition', 'COMPETITION'),
	('Outreach', 'OUTREACH'),
	('Fundraising', 'FUNDRAISING'),
	('Others', 'OTHERS'),
)
'''
SCOPE_CHOICES = (
	('program-restricted', 'PROGRAM-RESTRICTED'),
	('college-restricted', 'COLLEGE-RESTRICTED'),
	('university-wide', 'UNIVERSITY-WIDE'),
	('open to all', 'OPEN TO ALL'),
)
'''

DEG_CHOICES = (
	("B Landscape Architecture", "B Landscape Architecture"),
	("BS Architecture", "BS Architecture"),
	("BA Art Studies", "BA Art Studies"),
	("BA Comparative Literature", "BA Comparative Literature"),
	("BA Creative Writing", "BA Creative Writing"), 
	("BA English Studies", "BA English Studies"),
	("BA European Languages", "BA European Languages"),
	("BA Araling Pilipino", "BA Araling Pilipino"),
	("BA Filipino", "BA Filipino"),
	("BA Malikhaing Pagsulat sa Filipino", "BA Malikhaing Pagsulat sa Filipino"),
	("BA Speech Communication", "BA Speech Communication"),
	("BA Theatre Arts", "BA Theatre Arts"),
	("BS Tourism", "BS Tourism"),
	("BS Business Administration", "BS Business Administration"),
	("BS Business Administration & Accountancy", "BS Business Administration & Accountancy"), 
	("BS Business Economics", "BS Business Economics"),
	("BS Economics", "BS Economics"),
	("B Elementary Education", "B Elementary Education"),
	("B Secondary Education", "B Secondary Education"),
	("BS Chemical Engineering", "BS Chemical Engineering"),
	("BS Civil Engineering", "BS Civil Engineering"),
	("BS Computer Science", "BS Computer Science"),
	("BS Computer Engineering", "BS Computer Engineering"),
	("BS Electrical Engineering", "BS Electrical Engineering"),
	("BS Electronics Engineering", "BS Electronics Engineering"),
	("BS Geodetic Engineering", "BS Geodetic Engineering"),
	("BS Industrial Engineering", "BS Industrial Engineering"),
	("BS Mechanical Engineering", "BS Mechanical Engineering"),
	("BS Mining Engineering", "BS Mining Engineering"),
	("BS Metallurgical Engineering", "BS Metallurgical Engineering"),
	("BS Materials Engineering", "BS Materials Engineering"),
	("BFA Painting", "BFA Painting"),
	("BFA Sculpture", "BFA Sculpture"),
	("BFA Art Education", "BFA Art Education"),
	("BFA Art History", "BFA Art History"),
	("BFA Industrial Design", "BFA Industrial Design"),
	("BFA Visual Communication", "BFA Visual Communication"),
	("BS Interior Design", "BS Interior Design"),
	("BS Clothing Technology", "BS Clothing Technology"),
	("BS Family Life & Child Development", "BS Family Life & Child Development"),
	("BS Community Nutrition", "BS Community Nutrition"),
	("BS Food Technology", "BS Food Technology"),
	("BS Home Economics", "BS Home Economics"),
	("BS Hotel, Restaurant & Institution Management", "BS Hotel, Restaurant & Institution Management"),
	("B Physical Education", "B Physical Education"),
	("B Sports Science", "B Sports Science"),
	("B Library & Information Science", "B Library & Information Science"), 
	("BA Broadcast Communication", "BA Broadcast Communication"),
	("BA Communication Research", "BA Communication Research"),
	("BA Film", "BA Film"), 
	("BA Journalism", "BA Journalism"),
	("B Music", "B Music"),
	("BA Public Administration", "BA Public Administration"),
	("BS Biology", "BS Biology"),
	("BS Chemistry", "BS Chemistry"),
	("BS Mathematics", "BS Mathematics"),
	("BS Molecular Biology & Biotechnology", "BS Molecular Biology & Biotechnology"),
	("BS Geology", "BS Geology"),
	("BS Applied Physics", "BS Applied Physics"), 
	("BS Physics", "BS Physics"),
	("BA Anthropology", "BA Anthropology"), 
	("BS Geography", "BS Geography"),
	("BA History", "BA History"),
	("BA Linguistics", "BA Linguistics"), 
	("BA Philosophy", "BA Philosophy"), 
	("BA Political Science", "BA Political Science"),
	("BA Psychology", "BA Psychology"),
	("BS Psychology", "BS Psychology"),
	("BA Sociology", "BA Sociology"),
	("BS Community Development", "BS Community Development"), 
	("BS Social Work", "BS Social Work"), 
	("BS Statistics", "BS Statistics"),
)

COLLEGE_CHOICES = (
	("College of Architecture", "College of Architecture"),
	("College of Arts and Letters", "College of Arts and Letters"),
	("Asian Institute of Tourism", "Asian Institute of Tourism"),
	("College of Business Administration", "College of Business Administration"),
	("School of Economics", "School of Economics"),
	("College of Education", "College of Education"),
	("College of Engineering", "College of Engineering"),
	("College of Fine Arts", "College of Fine Arts"),
	("College of Home Economics", "College of Home Economics"),
	("College of Human Kinetics", "College of Human Kinetics"),
	("School of Library and Information Sciences", "School of Library and Information Sciences"),
	("College of Mass Communication", "College of Mass Communication"),
	("College of Music", "College of Music"),
	("National College of Public Administration and Governance", "National College of Public Administration and Governance"),
	("College of Science", "College of Science"),
	("College of Social Sciences and Philosophy", "College of Social Sciences and Philosophy"),
	("College of Social Work and Community Development", "College of Social Work and Community Development"),
	("School of Statistics", "School of Statistics"),
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
	
	deg_prog = models.CharField(max_length = 50, default="N/A", blank=True, null=True, choices=DEG_CHOICES)
	college = models.CharField(max_length = 50, default="N/A", blank=True, null=True, choices=COLLEGE_CHOICES)
	#scope = models.CharField(max_length = 50, default=None, blank=True, null=True, choices=SCOPE_CHOICES)
	

	limit = models.IntegerField(default=None, blank=True, null=True)
	author = models.ForeignKey(User, default = None, on_delete = models.CASCADE)

	participants = models.ManyToManyField(User, blank=True, related_name = "events_joined")

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('event-detail', kwargs = {'pk': self.pk})


class Announcement(models.Model):
	date_posted = models.DateTimeField(default = timezone.now)
	subject = models.CharField(max_length = 500, default=None, blank=True, null=True)
	body = models.TextField()
	event = models.ForeignKey(Event, default = None, on_delete = models.CASCADE)
	author = models.ForeignKey(User, default = None, on_delete = models.CASCADE)

	def __str__(self):
		return str(self.pk)

	def get_absolute_url(self):
		return reverse('maincalendar')
