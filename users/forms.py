from django import forms
from django.contrib.auth.models import User

class  userUpdateForm(forms.ModelForm):
    first_name=forms.CharField(
        label="First Name",
        max_length=50,
        required=False
    )
    last_name=forms.CharField(
        label="Last Name",
        max_length=50,
        required=False
    )

    username=forms.CharField(
            label="User Name",
            max_length=50,
        
    )

    class Meta:
        model=User
        fields=['first_name','last_name','username']
