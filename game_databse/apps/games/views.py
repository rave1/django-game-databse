from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views import View
from django.conf import settings
from games.forms import GameForm
from rest_framework.generics import CreateAPIView
import requests
from games.models import Game
from games.serializers import GameSerializer


class TestTemplateView(TemplateView):
    template_name = 'test.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['api_key'] = settings.RAWG_API_KEY
        return context

    def get(self, request, *args, **kwargs):
        if request.htmx:
            kwargs['search_input'] = request.GET.get('q', None)
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
    

class SearchTemplateView(TemplateView):
    template_name = 'results.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.htmx:
            search = request.GET.get('q', None)
            if search:
                url = f'{settings.RAWG_API_URL}games'
                response = requests.get(url, params={'key': settings.RAWG_API_KEY, 'search': search, 'page_size': 10})
                response.raise_for_status()
                kwargs['data'] = response.json()['results']
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class AddGameView(CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class LibraryView(ListView):
    model = Game
