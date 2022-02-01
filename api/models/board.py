from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=128)

    def serialize(self):
        return {"name": self.name}

    def __str__(self):
        return self.name
