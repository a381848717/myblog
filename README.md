# myblog
1.0版本 
URL：re_path(r'^articles/$', views.ArticleList.as_view()),   # .../blog/articles/
    re_path(r'^articles/(?P<pk>[0-9]+)$', views.ArticleDetail.as_view()),   # .../blog/articles/2
