#from PIL import Image
from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')
class UploadFileForm(forms.Form):
	title = forms.CharField(max_length=50)
	picture = forms.ImageField()
