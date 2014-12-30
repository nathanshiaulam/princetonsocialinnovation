from django.contrib import admin
from psibackend.models import *

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'date');
	list_filter = ['date'];
	search_fields = ['title'];

class EventAdmin(admin.ModelAdmin):
	list_display = ('title', 'date');
	list_filter = ['date'];
	search_fields = ['title'];

class MemberAdmin(admin.ModelAdmin):
	list_display = ('name', 'thumb', 'position', 'year', 'current');
	search_fields = ['name'];

class ContactAdmin(admin.ModelAdmin):
	list_display = ('email', 'subject', 'message');
	search_fields = ['subject'];

admin.site.register(Event, EventAdmin);
admin.site.register(Post, PostAdmin);
admin.site.register(Member, MemberAdmin);
admin.site.register(Contact, ContactAdmin);
admin.site.register(Internship);
# Register your models here.

# nathanlam
# normal pw