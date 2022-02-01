from django.db import models

from .folder import Folder


class TodoItem(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField("Tags", blank=True, default=None)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def serialize(self):
        return {"name": self.name, "description": self.description, "tags": self.tags}
