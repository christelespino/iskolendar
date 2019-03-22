#This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2015-2016
'''
03/22/19
	Patrick Joseph Sanchez
		added the profile model
'''

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	student_number = models.CharField(max_length = 100, default="", null = False)
	name = models.CharField(max_length = 10, default="", null = False)
	position = models.CharField(max_length = 100, default="", null = False)
	organization = models.CharField(max_length = 100, default="", null = False)
	org_acronym = models.CharField(max_length = 10, default="", null = False)
	degree_program = models.CharField(max_length = 100, default="", null = False)

	user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name = "profile",
    )

	def __str__(self):
		return self.name
	'''
	def get_absolute_url(self):
		return reverse('event-detail', kwargs = {'pk': self.pk})
	'''

# Create your models here.
