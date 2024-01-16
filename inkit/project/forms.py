from collections.abc import Mapping
from typing import Any
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django import forms
from django.forms.utils import ErrorList

from .models import project 

class projectForm(ModelForm):
    class Meta:
        model = project
        fields = ['title','featured_image','description','demo_link','source_link','tags']
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }
    
    def __init__(self,*args, **kwargs):
        super(projectForm,self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update()