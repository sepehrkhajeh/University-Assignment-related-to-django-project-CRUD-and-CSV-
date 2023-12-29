from django import forms
from .models import UploadFileModel

class FileForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ['file',]