from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from django import template

# create your models here

class Post(models.Model):
    title = models.CharField(max_length=150);
    body = models.TextField();
    picture = models.ImageField(upload_to='news/', blank=True, null=True);
    croppedPicture = models.ImageField(upload_to='news/', blank=True, null=True);
    date = models.DateField('date posted');

    def thumb(self):
        if self.picture:
            return mark_safe(u'<img src="%s" width=60 height=60 />' % (self.picture.url));
        else:
            return mark_safe('No image file found');

    def __unicode__(self):
        return self.title;


class Event(models.Model):
    title = models.CharField(max_length=150);
    location = models.CharField(max_length=150);
    picture = models.ImageField(upload_to='events/', blank=True, null=True);
    date = models.DateTimeField('time of event');
    white = models.BooleanField(default=False);
    identifier = models.CharField(default="", max_length=100);
    description = models.TextField();

    def thumb(self):
        if self.picture:
            return mark_safe(u'<img src="%s" width=60 height=60 />' % (self.picture.url));
        else:
            return mark_safe('No image file found');

    def __unicode__(self):
        return self.title;

class Internship(models.Model):
    intern_role = models.CharField(max_length=150, default=None, blank=True);
    email = models.EmailField(max_length=150, default=None, blank=True);
    employer = models.CharField(max_length=150);
    description = models.TextField();
    approved = models.BooleanField(default=False);

    def __unicode__(self):
        return self.intern_role;

class Member(models.Model):
    name = models.CharField(max_length=150); 
    year = models.CharField(max_length=150);
    picture = models.ImageField(upload_to='members/', blank=True, null=True);
    funnypicture = models.ImageField(upload_to='members/', blank=True, null=True);
    position = models.CharField(max_length=150);
    bio = models.TextField();
    current = models.BooleanField(default=True);

    def thumb(self):
        if self.picture:
            return mark_safe(u'<img src="%s" width=60 height=60 />' % (self.picture.url));
        else:
            return mark_safe('No image file found');
           
    def __unicode__(self):
        return self.name;

class Contact(models.Model):
    email = models.EmailField(max_length=150, default=None, blank=True);
    subject = models.CharField(max_length=150, default=None, blank=True);
    message = models.TextField();

    def __unicode__(self):
        return self.subject;

