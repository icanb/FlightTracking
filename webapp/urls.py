

from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.contrib.auth.views import logout
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.core.urlresolvers import reverse
from django.views.generic import RedirectView


urlpatterns = patterns('webapp.pages',
                       url(r'^$', 'homepage'),
                       url(r'^My_Flights/$', 'my_flights'),
                       url(r'^Edit_Flight/(\d+)/$', 'edit_flight'),
                       url(r'^All_Flights/$', 'all_flights'),
                       url(r'^Houses/$', 'houses'),
                       url(r'^House_Page/(\d+)/$', 'house_page'),
                       url(r'^sdf_page/$', 'sdf_page'),
                       url(r'^Signup_Page/$', 'signup_page'),
                       url(r'^About_Us/$', 'about_us'),
                       url(r'^People/$', 'people'),
                       url(r'^Profile_PAge/(\d+)/$', 'profile_page'),
                       )


urlpatterns += patterns('webapp.form_receivers',
                        url('^__form_receiver/loginform/$', 'login'),
                        url(u'^__facebook_social_auth_callback/$', lambda r:
                            RedirectView.as_view(
                                url=reverse('webapp.pages.my_flights'))(r)),
                        url('^__form_receiver/create_flight/$', 'create_flight'),
                        url('^__form_receiver/edit_flight/(\\d+)/$', 'edit_flight'),
                        url('^__form_receiver/create_house/$', 'create_house'),
                        url('^__form_receiver/shortsignupform/$', 'sign_up'),
                        )


admin.autodiscover()

urlpatterns += patterns('',
                        url(r'', include("social_auth.urls")),
                        url(r'^admin/', include(admin.site.urls)),
                        url(r'^grappelli/', include('grappelli.urls')),
                        url(r'^__logout/$', logout, kwargs={'next_page': '/'}),
                        )
