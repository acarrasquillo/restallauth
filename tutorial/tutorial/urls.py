from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from allauth.account.views import ConfirmEmailView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^account-confirm-email/(?P<key>\w+)/$', ConfirmEmailView.as_view()	, name='account_confirm_email'),
)