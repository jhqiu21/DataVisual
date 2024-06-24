from django import forms
from .models import UploadedFile

# upload file form
class UploadFileForm(forms.ModelForm):
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'custom-file-input',
            'id': 'customFile'
        })
    )
    
    title = forms.CharField(
        min_length=0,
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the plot title here'
        })
    )

    class Meta:
        model = UploadedFile
        fields = ['file', 'title']
        