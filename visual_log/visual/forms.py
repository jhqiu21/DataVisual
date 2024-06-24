from django import forms
from .models import UploadedFile

# upload file form
class UploadFileForm(forms.ModelForm):
    file = forms.FileField()
    class Meta:
        model = UploadedFile
        fields = ['file']
        