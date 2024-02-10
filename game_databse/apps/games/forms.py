from django.forms import ModelForm
from games.models import Game


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = (
            'name', 'image', 'platform', 'users'
        )
