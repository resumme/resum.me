from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
import datetime
from django.dispatch import receiver
import requests
from django.db import models
from taggit.managers import TaggableManager


class Provider(models.Model):
    """
    A provider is a Course provider, like
    Codeschool, Pluralsight ...
    """
    name = models.CharField(max_length=32)
    enabled = models.BooleanField(default=False)
    icon = models.ImageField(upload_to='providers/', blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    """
    Each course of each Provider
    """
    title = models.CharField(max_length=128, blank=True)
    url = models.CharField(max_length=256, blank=True)
    badge = models.CharField(max_length=256, blank=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=256, blank=True)
    country = models.CharField(max_length=256, blank=True)
    mail = models.CharField(max_length=128, blank=True)
    bio = models.TextField(max_length=2048, blank=True)
    occupation = models.CharField(max_length=256, blank=True)
    resume = models.TextField(max_length=2048, blank=True)
    birth_date = models.DateField(null=True, blank=True, default=datetime.date.today)

    avatar = models.ImageField(upload_to='avatars/', blank=True)

    @property
    def full_name(self):
        return ' '.join([self.first_name, self.last_name])

    @property
    def location(self):
        return ', '.join([self.city, self.country])


class ProviderProfile(models.Model):
    """
    Profile of the user in each Provider.
    The user will tipically have an account for
    each provider.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username_provider = models.CharField(max_length=30, blank=True)
    courses = models.ManyToManyField(Course, through='CourseStatus')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    error = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.provider)

    class Meta:
        unique_together = ('user', 'provider',)


class CourseStatus(models.Model):
    """
    Each course of each profile has an status
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    profile = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)


class TimelineItem(models.Model):
    """
    Timeline items of the CV
    """
    CHOICES = (
        ('j', 'Job'),
        ('f', 'Formation - College, school, bootcamp...'),
        ('e', 'Event - Hackatons, conferences...'),
        ('c', 'Certifications - External certificates'),
    )
    type = models.CharField(max_length=1, choices=CHOICES)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.type == 'j':
            return 'New Job'
        if self.type == 'f':
            return 'Formation'
        if self.type == 'e':
            return 'Event'
        if self.type == 'c':
            return 'Certification'
