from django.urls import path
from .views import EventDetailView, EventCreateView#, EventUpdateView, EventDeleteView
from . import views

urlpatterns = [
    #path('', EventListView.as_view(), name='maincalendar'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/new/', EventCreateView.as_view(), name='event-create'),
    #path('event/<int:pk>/update', EventUpdateView.as_view(), name='event-update'),
    #path('event/<int:pk>/delete', EventDeleteView.as_view(), name='event-delete'),
    
    path('', views.maincalendar, name = 'maincalendar'),
]
