# myblog
1.0版本 


URL：
<h4> .../blog/articles/ </h4>
re_path(r'^articles/$', views.ArticleList.as_view()),
<h4> .../blog/articles/2 </h4>
re_path(r'^articles/(?P<pk>[0-9]+)$', views.ArticleDetail.as_view()),
