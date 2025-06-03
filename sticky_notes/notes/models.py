from django.db import models


# Create your models here.
class Note(models.Model):
    """
    Model representing a note.

    Fields:
    - title: The title of the note.
    - content: The content of the note.
    - created_at: The date and time when the note was created.
    - updated_at: The date and time when the note was last updated.

    Methods:
    - __str__: Returns a string representation of the note (the title).

    :param models.Model: Django's base model class.
    """

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
