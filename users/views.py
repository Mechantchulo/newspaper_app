from django.shortcuts import render

# Import CreateView from Django's generic views module
from django.views.generic import CreateView

# Import reverse_lazy for resolving URLs lazily (i.e., when they are needed)
from django.urls import reverse_lazy

# Import the custom user creation form that you have created
from .forms import CustomUserCreationForm

# Define a class-based view for user sign-up
class SignUpView(CreateView):
    # Specify the form class that this view will use
    form_class = CustomUserCreationForm
    # Define the URL to redirect to after the form is successfully submitted
    # reverse_lazy is used here to delay the URL resolution until it is needed
    success_url = reverse_lazy('login')
    # Specify the template that will be used to render this view
    template_name = 'signup.html'
