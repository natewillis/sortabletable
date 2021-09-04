from django import forms
from .models import TableRow


class TableRowForm(forms.ModelForm):
    class Meta:
        model = TableRow
        fields = (
            'first_name',
            'last_name',
            'home_state',
            'age'
        )
