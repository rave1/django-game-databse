from typing import Any
from django.views.generic.base import TemplateView
from django.conf import settings


class TestTemplateView(TemplateView):
    template_name = 'test.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['api_key'] = settings.RAWG_API_KEY
        return context