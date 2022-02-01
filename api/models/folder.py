from django.db import models
from .board import Board


class Folder(models.Model):
    name = models.CharField(max_length=128, default="BaseFolder")
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def serialize(self):
        return {"name": self.name, "description": self.description}
