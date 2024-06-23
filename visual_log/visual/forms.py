from django import forms
from .models import UploadedFile

# upload file form
class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']
        