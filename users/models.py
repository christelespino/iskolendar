#This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2015-2016
'''
03/22/19
	Patrick Joseph Sanchez
		added the profile model
'''

from django.db import models
from django.contrib.auth.models import User
from maincalendar.models import Event

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
	("12", "Materials Engineering"),
	("13", "Biology")
]

COLLEGE_CHOICES = (
	("1", "College of Engineering"),
	("2", "College of Science"),
)

class Profile(models.Model):
	student_number = models.CharField(max_length = 100, default="", null = False)
	name = models.CharField(max_length = 10, default="", null = False)
	position = models.CharField(max_length = 100, default="", null = False)
	organization = models.CharField(max_length = 100, default="", null = False)
	org_acronym = models.CharField(max_length = 10, default="", null = False)
	college = models.CharField(max_length = 100, default="", null = False, choices = COLLEGE_CHOICES)
	degree_program = models.CharField(max_length = 100, default="", null = False)

	user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name = "profile",
    )

	bookmarks = models.ManyToManyField(Event, blank=True, related_name = "bookmarked")
	
	def __str__(self):
		return self.name
	'''
	def get_absolute_url(self):
		return reverse('event-detail', kwargs = {'pk': self.pk})
	'''
 
# Create your models here.
