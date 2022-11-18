from django.urls import path
from .views import SongAPIView, ArtistAPIView, GenreAPIView, AlbumAPIView, PlaylistAPIView

urlpatterns = [
    path('song/', SongAPIView.as_view()),
    path('song/<str:pk>/', SongAPIView.as_view()),
    path('artist/', ArtistAPIView.as_view()),
    path('artist/<str:pk>/', ArtistAPIView.as_view()),
    path('genre/', GenreAPIView.as_view()),
    path('genre/<str:pk>/', GenreAPIView.as_view()),
    path('album/', AlbumAPIView.as_view()),
    path('album/<str:pk>/', AlbumAPIView.as_view()),
    path('playlist/', PlaylistAPIView.as_view()),
    path('playlist/<str:pk>/', PlaylistAPIView.as_view()),

    path('artistsonglist/', ArtistSongList.as_view()),
    path('artistsonglist/<str:pk>', ArtistSongDetail.as_view()),
    path('albumsong/', AlbumSongList.as_view()),
    path('albumsong/<str:pk>', AlbumSongDetail.as_view())
]