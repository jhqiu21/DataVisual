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
        initial='Plot' ,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the plot title here'
        })
    )

    tfont = forms.fields.IntegerField(
        initial=24,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    style = forms.CharField(
        min_length=0,
        max_length=30,
        initial='seaborn-v0_8-paper' ,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'y-axis title'
        })
    )

    xtitle = forms.CharField(
        min_length=0,
        max_length=30,
        initial='x-axis title' ,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'x-axis title'
        })
    )

    xfont = forms.fields.IntegerField(
        initial=14,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    ytitle = forms.CharField(
        min_length=0,
        max_length=30,
        initial='y-axis title' ,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'y-axis title'
        })
    )

    yfont = forms.fields.IntegerField(
        initial=14,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    legend = forms.fields.ChoiceField(
        choices=(
            (1, "Yes"), 
            (2, "No"), 
        ),
        label="type",
        initial=1,
        widget=forms.widgets.Select(attrs={
            'class': 'form-select'
        })
    )

    type = forms.fields.ChoiceField(
        choices=(
            (1, "Histogram"), 
            (2, "Bihistogram"), 
            (3, "Cumulative distributions"), 
            (4, "Line Chart"), 
            (5, "Confidece Ellipse"),
        ),
        label="type",
        initial=1,
        widget=forms.widgets.Select(attrs={
            'class': 'form-select'
        })
    )

    bin = forms.fields.IntegerField(
        initial=10,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    parameter = forms.CharField(
        min_length=0,
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Inplut parameters"
        })
    )

    class Meta:
        model = UploadedFile
        fields = ['file', 
                  'title', 
                  'tfont', 
                  'style', 
                  'xtitle', 
                  'xfont', 
                  'ytitle', 
                  'yfont', 
                  'legend',
                  'type', 
                  'bin',
                  'parameter'
                  ]

