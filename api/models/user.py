from django.db import models as db_models
from django.contrib.auth import models as auth_models
from .board import Board


class User(db_models.Model):
    user = db_models.OneToOneField(auth_models.User, on_delete=db_models.CASCADE)
    # For now a user can only have 1 board.
    board = db_models.ForeignKey(Board, on_delete=db_models.CASCADE, unique=True)
