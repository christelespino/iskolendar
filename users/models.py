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
]

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
