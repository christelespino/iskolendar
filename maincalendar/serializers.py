from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
#from .models import Event, Announcement
#from rest_framework import serializers



class EventSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Event
        fields = ('id', 'title', 'date_posted',	'date_start', participants)


class UserSerializer(serializers.ModelSerializer):
    event_list = EventSerializer(many=True, read_only=True)

    class Meta:
        model = User 
        fields = ('id', 'name', 'events')