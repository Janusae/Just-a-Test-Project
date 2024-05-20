from django import forms
from .models import User_plus
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User_plus
        fields = "__all__"
        exclude = ["user"]