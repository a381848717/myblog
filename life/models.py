from django.db import models

# Create your models here.


class Album(models.Model):

    STATUS_CHOICES = (
        ('p', 'Published'),
        ('d', 'Draft'),
    )

    album_title = models.CharField(max_length=20, verbose_name="相册标题", default='默认相册', null=True, blank=True)
    album_intro = models.TextField(verbose_name="相册引言", blank=True)
    create_date = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    status = models.CharField('Status (*)', max_length=1, choices=STATUS_CHOICES, default='p', null=True, blank=True)

    def __str__(self):
        return self.album_title

    def meta(self):
        ordering = ['-create_date']
        verbose_name = "PhotoAlbum"
        verbose_name_plural = "PhotoAlbum"


class Photo(models.Model):
    photo_belong = models.ForeignKey("Album", verbose_name="归属相册", on_delete=models.CASCADE)
    photo_title = models.CharField(max_length=20, verbose_name="照片标题", blank=True)
    photo_intro = models.TextField(verbose_name="照片引言", blank=True)
    photo_url = models.CharField(max_length=512, verbose_name="图片链接", blank=True)
    pubdate = models.DateTimeField(verbose_name='上传日期', auto_now_add=True)

    def __str__(self):
        return self.photo_title

    def meta(self):
        ordering = ['-pubdate']
        verbose_name = "Photos"
        verbose_name_plural = "Photos"
