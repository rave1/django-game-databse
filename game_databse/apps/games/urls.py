from django.urls import path

from games.views import TestTemplateView, SearchTemplateView

urlpatterns = [
    path('', TestTemplateView.as_view(), name='home'),
    path('search/', SearchTemplateView.as_view(), name='game-search')
]
