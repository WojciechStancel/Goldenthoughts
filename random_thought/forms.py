from django import forms

from .models import GoldenThougthData


class GoldenForm(forms.ModelForm):
    class Meta:
        model = GoldenThougthData
        fields = ['name',
                  'body',
                  'category',
                  'added_by']

    def __repr__(self):
        return self.body
