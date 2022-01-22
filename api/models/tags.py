from django.db import models

# To get all tags in a borard use:
#   Tags.objects.get(board=user_board)

# User defined tags
class Tags(models.Model):
    name = models.CharField(max_length=128)
    board = models.ForeignKey("Board", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
