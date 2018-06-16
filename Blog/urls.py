from django.conf.urls import url
from . import views as my_views
urlpatterns = [
    url(r'^$', my_views.blogi, name='Blogi'),
    url(r'^post/(?P<pk>(\d+))/(?P<id_blogu>(\d+))/author/$', my_views.post_author, name='post_author'),
    url(r'^posts/(?P<pk>\d+)$', my_views.post_list, name='post_list'),
    url(r'^post/(?P<pk>(\d+))/(?P<id_blogu>(\d+))/$', my_views.post_detail, name='post_detail'),
    url(r'^blog/new/$', my_views.blog_new, name="blog_new"),
    url(r'^post/new/(?P<pk>\d+)/$', my_views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/(?P<id_blogu>(\d+))/edit/$', my_views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/(?P<id_blogu>\d+)/comment/$', my_views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<com_id>\d+)/(?P<pk>\d+)/(?P<id_blogu>\d+)/comment/$', my_views.add_comment_to_comment,
        name='add_comment_to_comment'),
]
