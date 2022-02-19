from django.urls import path

from .views import auth, board, user

urlpatterns = [
    # No home for /api route.
    path("users/", user.UsersView.as_view()),
    path("users/<int:id>/", user.UsersView.as_view()),
    path("login/", auth.LoginView.as_view()),
    path("logout/", auth.LogoutView.as_view()),
    path("board/", board.BoardsView.as_view()),
]
