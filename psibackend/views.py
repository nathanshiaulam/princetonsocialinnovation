from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.core.mail import send_mail, BadHeaderError
from django.template import RequestContext

from psibackend.models import *
from psibackend.forms import *

class HomeView(generic.ListView):
	template_name = 'psibackend/index.html';
	context_object_name = 'all_posts';

	def get_queryset(self):
		"""Return the last five published posts."""
		queryset = Post.objects.filter();
		return queryset.reverse()[:3]

class AboutView(generic.ListView):
	template_name = 'psibackend/about.html';
	context_object_name = 'all_members';

	def get_queryset(self):
		return Member.objects.filter();

class MembersDetailView(generic.DetailView):
	model = Member;
	template_name = 'psibackend/membersdetail.html';

	def get_queryset(self):
		return Member.objects.filter();

	def get_absolute_url(self):
		return reverse('membersdetail', kwargs={'pk':self.id});

class EventsView(generic.ListView):
	template_name = 'psibackend/events.html';
	context_object_name = 'all_events';

	def get_queryset(self):
		return Event.objects.all().order_by('-date');

def NewsView(request):
	latest_news_post = Post.objects.order_by('-date')[1:5];
	all_posts = Post.objects.all().order_by('-date');
	first_news_post = Post.objects.order_by('-date')[:1];

	return render(request, "psibackend/news.html", {
		'latest_news_post':latest_news_post,
		'all_posts':all_posts,
		'first_news_post':first_news_post
		});


class NewsDetailView(generic.DetailView):
	model = Post;
	template_name = 'psibackend/newsdetail.html';

	def get_queryset(self):
		return Post.objects.filter();

	def get_absolute_url(self):
		return reverse('newsdetail', kwargs={'pk':self.id});

class InternshipsView(generic.ListView):
	template_name = 'psibackend/internships.html';
	context_object_name = 'all_internships';

	def get_queryset(self):
		return Internship.objects.filter();

class InternshipsDetailView(generic.DetailView):
	model = Internship;
	template_name = 'psibackend/internshipsdetail.html';

	def get_queryset(self):
		return Internship.objects.filter();

	def get_absolute_url(self):
		return reverse('internshipsdetail', kwargs={'pk':self.id});

def contact_view(request):
	if request.method == "POST":
		form = ContactForm(request.POST);
		if form.is_valid():
			contact = form.save();
			return redirect('/thankyou_contact', pk=contact.pk);
	else:
		form = ContactForm();
	return render(request, 'psibackend/contact.html', {'form':form});

def internship_post(request):
	if request.method == "POST":
		form = InternshipForm(request.POST);
		if form.is_valid():
			internship = form.save();
			return redirect('/thankyou_intern', pk=internship.pk); # change to internship page
	else:
		form = InternshipForm();
	return render(request, 'psibackend/findinterns.html', {'form': form});

def thankyou_intern(request):
		return render_to_response('psibackend/thankyou_intern.html')

def thankyou_contact(request):
		return render_to_response('psibackend/thankyou_contact.html')





