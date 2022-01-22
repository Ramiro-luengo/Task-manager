from django.db import models
from .board import Board


class Folder(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class BaseFolder(Folder):
    name = models.CharField(max_length=128, default="BaseFolder")

    class Meta:
        proxy = True
