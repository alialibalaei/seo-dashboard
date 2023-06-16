from django.urls import path
from .views import SignupPageView ,ChangepasswordPageView

urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
        path("accounts/password_change/", ChangepasswordPageView.as_view(), name="password_change"),
]