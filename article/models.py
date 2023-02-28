from django.db import models

# Create your models here.


class Article(models.Model):
    TOPIC_CHOICES = (
        ('p', 'Python'),
        ('g', 'GO'),
        ('n', 'News'),
    )

    STATUS_CHOICES = (
        ('p', 'Published'),
        ('d', 'Draft'),
    )

    article_topic = models.CharField(max_length=1, verbose_name="话题", choices=TOPIC_CHOICES, default='P', null=True, blank=True)
    article_title = models.CharField(max_length=50, verbose_name="标题")
    article_author = models.CharField(max_length=20, verbose_name="作者", default="茉茉")
    article_body = models.TextField(verbose_name="内容", blank=True)
    create_date = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    status = models.CharField('Status (*)', max_length=1, choices=STATUS_CHOICES, default='P', null=True, blank=True)

    def __str__(self):
        return self.article_title

    def meta(self):
        ordering = ['-create_date']
        verbose_name = "Article"
        verbose_name_plural = "Articles"
# 姓名、性别、年龄、民族、籍贯、政治面貌、学历、联系方式，以及自我评价、工作经历、学习经历、荣誉与成就、求职愿望、对这份工作的简要理解等等