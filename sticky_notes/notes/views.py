# notes/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


# Create your views here.
def note_list(request):
    '''
    View function to display a list of all notes.

    :param request: The HTTP request object.
    :return: Rendered HTML page with the list of notes.
    '''
    # Fetching all notes from the database

    notes = Note.objects.all()

    # Creating a context dictionary to pass data
    context = {
        "notes": notes,
        "page_title": "List of Notes",
    }

    return render(request, "notes/note_list.html", context)


def note_detail(request, pk):
    """
    View function to display the details of a specific note.

    :param request: The HTTP request object.
    :param pk: The primary key of the note to display.
    :return: Rendered HTML page with the note details.
    """
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


def note_create(request):
    """
    View function to create a new note.

    :param request: The HTTP request object.
    :return: Rendered HTML page with the note creation form.
    """

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect("note_list")
    else:
        form = NoteForm()
    return render(request, "notes/note_form.html", {"form": form})


def note_update(request, pk):
    """
    View function to update an existing note.

    :param request: The HTTP request object.
    :param pk: The primary key of the note to update.
    :return: Rendered HTML page with the note update form.
    """
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect("note_list")
    else:
        form = NoteForm(instance=note)
    return render(request, "notes/note_form.html", {"form": form})


def note_delete(request, pk):
    """
    View function to delete a specific note.

    :param request: The HTTP request object.
    :param pk: The primary key of the note to delete.
    :return: Redirect to the note list page after deletion.
    """

    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect("note_list")
