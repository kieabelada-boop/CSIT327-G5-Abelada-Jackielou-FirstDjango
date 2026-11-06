from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser

def add_bootstrap_classes(form):
    for field in form.fields.values():
        field.widget.attrs["class"] = "form-control"

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_bootstrap_classes(self)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "first_name",
            "last_name", "course")

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_bootstrap_classes(self)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "course")

class CampusAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_bootstrap_classes(self)
