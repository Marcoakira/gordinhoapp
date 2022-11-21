from django.forms import ModelForm

from app.models import Eleitor


# Create the form class.
class EleitorForm(ModelForm):
    class Meta:
        model = Eleitor
        fields = ['nome', 'cpf', 'associacao']
