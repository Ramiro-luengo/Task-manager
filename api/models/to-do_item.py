from django.db import models
from django.utils.translation import gettext_lazy
from .folder import Folder, BaseFolder
from jsonfield import JSONField


class TodoItem(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField("Tags", blank=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, default=BaseFolder)

    def __str__(self):
        return self.name
