from django.urls import path
from django.contrib.auth import views as auth_views

# Import the SignUpView from the views module
from .views import SignUpView

# Define the URL patterns for this application
urlpatterns = [
    # Map the URL path 'signup/' to the SignUpView
    # as_view() method is called on the class-based view to create an instance of the view
    # name='signup' gives this URL pattern a name, which can be used for URL reversing
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
