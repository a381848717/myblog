# myblog
1.0版本<br><br>
URL:
<h4> .../blog/articles/ </h4>
re_path(r'^articles/$', views.ArticleList.as_view()),
<h4> .../blog/articles/2 </h4>
re_path(r'^articles/(?P<pk>[0-9]+)$', views.ArticleDetail.as_view()),<br><br>
返回:<br>
{
    "id": 2,
    "article_topic": "Python",
    "status": "Published",
    "cn_status": "已发表",
    "create_date": "2022-12-05 18:08:36",
    "article_title": "浅谈http协议六种请求方法，get、head、put、delete、post、options区别",
    "article_author": "茉茉",
    "article_body": "标准Http协议支持六种请求方法，即......"
}
