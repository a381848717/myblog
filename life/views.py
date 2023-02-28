from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import Album, Photo
from .serializers import AlbumSerializer, PhotosSerializer


class AlbumList(APIView):
    """
    List all articles, or create a new article.
    """
    def get(self, request, format=None):
        album = Album.objects.all()
        serializer = AlbumSerializer(album, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            # 注意：手动将request.user与author绑定
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumDetail(APIView):
    """
    Retrieve, update or delete an article instance.
    """
    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = AlbumSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        album = self.get_object(pk)
        serializer = AlbumSerializer(instance=album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PhotosList(APIView):
    """
    List all articles, or create a new article.
    """
    def get(self, request, format=None):
        photos = Photo.objects.all()
        serializer = PhotosSerializer(photos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PhotosSerializer(data=request.data)
        if serializer.is_valid():
            # 注意：手动将request.user与author绑定
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhotosDetail(APIView):
    """
    Retrieve, update or delete an article instance.
    """
    def get_object(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        photos = self.get_object(pk)
        serializer = PhotosSerializer(photos)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        photos = self.get_object(pk)
        serializer = PhotosSerializer(instance=photos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
