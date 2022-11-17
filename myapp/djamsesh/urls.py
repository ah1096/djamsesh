from django.urls import path
from .views import SongAPIView, ArtistAPIView, GenreAPIView

urlpatterns = [
    path('song/', SongAPIView.as_view()),
    path('song/<str:pk>/', SongAPIView.as_view()),
    path('artist/', ArtistAPIView.as_view()),
    path('artist/<str:pk>/', ArtistAPIView.as_view()),
    path('genre/', GenreAPIView.as_view()),
    path('genre/<str:pk>/', GenreAPIView.as_view()),
]