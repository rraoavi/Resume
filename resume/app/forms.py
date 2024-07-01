from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'email', 'phone', 'state', 'city', 'block', 'house_number',
                  'education', 'experience', 'skills', 'languages', 'projects']