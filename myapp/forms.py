from django import forms 

class userforms(forms.Form):
    name=forms.CharField(max_length=100)
    phone=forms.CharField(max_length=60)
    city=forms.CharField(max_length=50)
    state=forms.CharField(max_length=40)
    email=forms.EmailField()
    message=forms.CharField(max_length=100)