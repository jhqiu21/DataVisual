from django import forms
from .models import UploadedFile

# upload file form
class UploadFileForm(forms.ModelForm):
    title = forms.CharField(min_length=0, max_length=50)
    file = forms.FileField()
    class Meta:
        model = UploadedFile
        fields = ['file']
        