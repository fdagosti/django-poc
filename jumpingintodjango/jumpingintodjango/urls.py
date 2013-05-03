from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^questions/$', 'questionsandanswers.views.index', name="questions"),

	url(r'^questions/(?P<question_id>\d+)/$', 'questionsandanswers.views.question_detail', name='question_detail'),
	url(r'^questions/create/$', 'questionsandanswers.views.question_create', name="question_create"),	
	url(r'^questions/edit/(?P<question_id>\d+)/$',
         'questionsandanswers.views.question_edit',
         name='question_edit'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^login/$', 'jumpingintodjango.views.login_page', name="login"),
	url(r'^$', 'jumpingintodjango.views.homepage', name="homepage"),
	url(r'^logout/$', 'jumpingintodjango.views.logout_view', name="logout"),

)
