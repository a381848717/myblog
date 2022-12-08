# myblog
1.0版本 


URL：
# .../blog/articles/
re_path(r'^articles/$', views.ArticleList.as_view()),
# .../blog/articles/2
re_path(r'^articles/(?P<pk>[0-9]+)$', views.ArticleDetail.as_view()),   
