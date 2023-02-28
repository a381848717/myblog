from django.contrib import admin
from .models import Album, Photo


# Register your models here.
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_title', 'album_intro', 'create_date', 'status')

    '''filter options'''
    list_filter = ('status',)

    '''10 items per page'''
    list_per_page = 10


admin.site.register(Album, AlbumAdmin)


class PhotosAdmin(admin.ModelAdmin):
    list_display = ('photo_title', 'photo_intro', 'photo_url', 'pubdate')

    '''filter options'''
    list_filter = ('pubdate',)

    '''10 items per page'''
    list_per_page = 10


admin.site.register(Photo, PhotosAdmin)
