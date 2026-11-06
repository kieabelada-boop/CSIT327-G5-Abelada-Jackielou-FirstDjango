from django.urls import path
from .views import CampusLoginView, ProfileUpdateView, SignUpView

urlpatterns = [
    path("login/", CampusLoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", ProfileUpdateView.as_view(), name="profile"),
]