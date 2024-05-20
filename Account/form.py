from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from werkzeug.routing import ValidationError

from .models import User_plus
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User_plus
        fields = "__all__"
        exclude = ["user"]
class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username" , "email"]
    def clean(self):
        cd = self.cleaned_data
        if cd["password1"] == cd["password2"]:
            return cd["password2"]
        else :
            raise ValidationError("Password and Confirm Password do not match")
