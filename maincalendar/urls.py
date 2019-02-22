#This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2015-2016
'''
02/05/2019
Patrick Joseph Sanchez
	added the url paths for the index, creating event and viewing the details of the event
02/06/2019
Christel Anne Espino
	added the url paths for updating event details and deleting event	
'''
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from .views import EventDetailView, EventCreateView, EventUpdateView, EventDeleteView
from . import views

urlpatterns = [
    #path('', EventListView.as_view(), name='maincalendar'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/new/', staff_member_required(EventCreateView.as_view()), name='event-create'),
    path('event/<int:pk>/update', EventUpdateView.as_view(), name='event-update'),
    path('event/<int:pk>/delete', EventDeleteView.as_view(), name='event-delete'),
    path('', views.maincalendar, name = 'maincalendar'),
    url(r'event/$', views.daily_view, name='daily-view'),
]
