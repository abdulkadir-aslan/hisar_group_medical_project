from django import forms
from django_recaptcha.fields import ReCaptchaField

class ContactForm(forms.Form):
    captcha = ReCaptchaField()
    name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Adı Soyadı',},))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'E-mail','type':'email'},))
    phone =  forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Telefon',},))
    subject = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Konu',},))
    content = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder':'Mesaj',
                'rows':2
            }))
    
class MeetingForm(forms.Form):
    captcha = ReCaptchaField()
    name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Adı Soyadı',},))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'E-mail','type':'email'},))
    phone =  forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Telefon',},))
    date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))
    time = forms.TimeField(widget=forms.TimeInput(format='%H:%M',attrs={'class': 'form-control','type':'time'}))