from django.conf.urls import url
from . import views as my_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout,{'template_name': 'logged_out.html'}, name='logout'),
    url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),
    url(r'^password-change/$',auth_views.password_change,{'template_name': 'password_change_form.html'},name='password_change'),
    url(r'^password-change/done/$',auth_views.password_change_done,{'template_name': 'password_change_done.html'},name='password_change_done'),

    url(r'^password-reset/$',
        auth_views.password_reset,
{'template_name': 'password_reset_form.html'},
        name='password_reset'),
    url(r'^password-reset/done/$',
        auth_views.password_reset_done,
{'template_name': 'password_reset_done.html'},
        name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        auth_views.password_reset_confirm,
{'template_name': 'password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^password-reset/complete/$',
        auth_views.password_reset_complete,
{'template_name': 'password_reset_complete.html'},
        name='password_reset_complete'),
    url(r'^register/$', my_views.register, name='register'),
url(r'^edit/$', my_views.edit, name='edit'),


]