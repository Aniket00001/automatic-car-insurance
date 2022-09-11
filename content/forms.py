from django import forms  
from .models import Documents


class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 10)  
    email     = forms.EmailField(label="Enter Email")  
    file      = forms.FileField() # for creating file input   

class DocumentForm(forms.ModelForm):
    document  = forms.FileField(widget = forms.FileInput, label = "")
    document1  = forms.FileField(widget = forms.FileInput, label = "")
    document2  = forms.FileField(widget = forms.FileInput, label = "")
    document3 = forms.FileField(widget = forms.FileInput, label = "")
    
    class Meta:
        model = Documents
        fields = [
            'document',
            'document1',
            'document2',
            'document3'
        ]
        widgets = {
            'document' : forms.FileInput(attrs={
                'class':"custom-file-input"
            }),
            'document1' : forms.FileInput(attrs={
                'class':"custom-file-input"
            }),
            'document2' : forms.FileInput(attrs={
                'class':"custom-file-input"
            }),
            'document3' : forms.FileInput(attrs={
                'class':"custom-file-input"
            })
        }
