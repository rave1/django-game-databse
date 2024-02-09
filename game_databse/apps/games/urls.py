from django.urls import path

from games.views import TestTemplateView

urlpatterns = [
    path('', TestTemplateView.as_view(), name='home')
]
