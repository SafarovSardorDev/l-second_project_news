from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField
from .models import News , Contact


class AddNewForms(forms.ModelForm):
    
    class Meta():
        model = News
        fields = ['title', 'body', 'img', 'category', 'tags']
        
class Contact_form(forms.ModelForm):
    class Meta :
        model = Contact
        fields = "__all__"
           