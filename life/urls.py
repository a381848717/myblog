from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from life import views

urlpatterns = [
    # re_path(r'^articles/$', views.article_list),
    # re_path(r'^articles/(?P<pk>[0-9]+)$', views.article_detail),
    re_path(r'^album/$', views.AlbumList.as_view()),
    re_path(r'^album/(?P<pk>[0-9]+)$', views.AlbumDetail.as_view()),
    re_path(r'^photos/$', views.PhotosList.as_view()),
    re_path(r'^photos/(?P<pk>[0-9]+)$', views.PhotosDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)