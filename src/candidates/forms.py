from django import forms

class zip_number(forms.Form):
    zip_code = forms.IntegerField(label='zip_code')