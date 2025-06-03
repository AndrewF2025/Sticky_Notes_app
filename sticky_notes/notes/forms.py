# notes/forms.py
from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """
    Form for creating and updating notes.

    Fields:
    - title: The title of the note.
    - content: The content of the note.

    Meta class:
    - Defines the model to use (Note) and the fields to include in the form.

    Widgets:
    - title: A text input with a CSS class for styling.
    - content: A textarea with a CSS class for styling.

    :param forms.ModelForm: Django's model form class.
    """

    class Meta:
        model = Note
        fields = ['title', 'content']
