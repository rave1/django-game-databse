from django.urls import path

from games.views import TestTemplateView, SearchTemplateView, AddGameView, LibraryView

urlpatterns = [
    path('', TestTemplateView.as_view(), name='home'),
    path('search/', SearchTemplateView.as_view(), name='game-search'),
    path('add-game/', AddGameView.as_view(), name='add-game'),
    path('library/', LibraryView.as_view(), name='game-library')
]
