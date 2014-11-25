from django.conf.urls import patterns, url

from django.conf import settings
from django.conf.urls.static import static

from psibackend import views

urlpatterns = patterns('',
	url(r'^$', views.HomeView.as_view(), name='index'),
	url(r'^about/$', views.AboutView, name='about'),
	url(r'^members/(?P<pk>\d+)/$', views.MembersDetailView.as_view(), name='membersdetail'),	
	url(r'^news/$', views.NewsView, name='news'),
	url(r'^news/(?P<pk>\d+)/$', views.NewsDetailView.as_view(), name='newsdetail'),	
	url(r'^events/$', views.EventsView.as_view(), name='events'),
	url(r'^internships/$', views.InternshipsView.as_view(), name='internships'),
	url(r'^internships/(?P<pk>\d+)/$', views.InternshipsDetailView.as_view(), name='internshipsdetail'),	
	url(r'^thankyou_intern/$', views.thankyou_intern, name='thankyou_intern'),
	url(r'^findinterns/$', views.internship_post, name='findinterns'),
	url(r'^contact/$', views.contact_view, name='contact'),
	url(r'^thankyou_contact/$', views.thankyou_contact, name='thankyou_contact'),
	url(r'^tedx/$', views.tedx_view, name='tedx'),
	
)+ static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
