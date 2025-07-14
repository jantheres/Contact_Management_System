from django import forms
from .models import Contact
import re

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    #  Add Bootstrap styling to all fields
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    #  Phone number validation: only 10 digits
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^\d{10}$', phone):
            raise forms.ValidationError("Phone number must be exactly 10 digits.")
        return phone

   