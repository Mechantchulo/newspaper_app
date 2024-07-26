from django import forms

# Import UserCreationForm and UserChangeForm from Django's built-in authentication forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Import the CustomUser model which you've defined in your models.py
from .models import CustomUser

# Define a form for creating new users, extending Django's built-in UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    # Meta class defines additional properties about the form
    class Meta(UserCreationForm):
        # Specify that this form is for the CustomUser model
        model = CustomUser
        # Include the fields from the base UserCreationForm and add a custom 'age' field
        fields = ('username', 'email', 'age',) #what will be listed in the admin url in the site

# Define a form for updating existing users, extending Django's built-in UserChangeForm
class CustomUserChangeForm(UserChangeForm):
    # Meta class defines additional properties about the form
    class Meta(UserChangeForm):
        # Specify that this form is for the CustomUser model
        model = CustomUser
        # Use the fields from the base UserChangeForm
        fields = ('username', 'email', 'age',) #what will be listed in the admin url in the site
