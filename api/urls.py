from django.urls import path, include

from .views import auth, user

# from django.http import HttpResponse


urlpatterns = [
    # No home for /api route.
    path("users/", user.UsersView.as_view()),
    path("users/<int:id>/", user.UsersView.as_view()),
    # TODO: Develop the rest of the accounts views since
    # it is gonna be handled by the front end.
    path("accounts/", include("django.contrib.auth.urls")),
    path("login/", auth.LoginView.as_view()),
]
