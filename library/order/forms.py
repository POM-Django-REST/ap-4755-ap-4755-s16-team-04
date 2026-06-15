from django import forms
from .models import Order


class OrderCreateForm(forms.Form):
    plated_end_at = forms.DateTimeField(
        label='Planned return date',
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local'},
            format='%Y-%m-%dT%H:%M'
        ),
        input_formats=['%Y-%m-%dT%H:%M'],
    )


class OrderEditForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['plated_end_at']
        widgets = {
            'plated_end_at': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['plated_end_at'].input_formats = ['%Y-%m-%dT%H:%M']