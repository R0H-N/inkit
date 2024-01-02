from django.forms import ModelForm

from .models import project 

class projectForm(ModelForm):
    class Meta:
        model = project
        fields = '__all__'