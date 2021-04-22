from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from . import models


class JobForm(forms.ModelForm):
    class Meta:
        model = models.Job
        fields = [
            'position',
            'name',
            'email',
            'location',
            'phone',
            'college',
            'graduation_year',
            'resume',
            'skills',
            'other_details',
            'github',
            'linkedin',
            'link',
            'expectations',
            'availability',
        ]