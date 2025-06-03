# notes/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Note


class NoteModelTest(TestCase):
    def setUp(self):
        # Create 2 Note object for testing
        Note.objects.create(
            title='Test Note',
            content='This is a test note.',
        )
        Note.objects.create(
            title='Test Note 2',
            content='This is another test note.',
        )

    def test_note_has_title(self):
        # Test that a Note object has the expected title
        post = Note.objects.get(id=1)
        self.assertEqual(post.title, 'Test Note')

    def test_note_has_content(self):
        # Test that a Note object has the expected content
        post = Note.objects.get(id=1)
        self.assertEqual(post.content, 'This is a test note.')

    def test_note_count(self):
        # Test that the number of Note objects created is correct
        count = Note.objects.count()
        # There should be 2 Note objects created in setUp
        self.assertEqual(count, 2)

    def test_note_delete(self):
        # Test that a Note object can be deleted
        post = Note.objects.get(id=2)
        post.delete()
        # Check if the post was deleted
        count = Note.objects.count()
        self.assertEqual(count, 1)

    def test_note_update(self):
        # Test that a Note object can be updated
        post = Note.objects.get(id=1)
        # Update the title and content of the post
        post.title = 'Updated Test Note'
        post.content = 'This is an updated test note.'
        post.save()
        # Fetch the updated post from the database
        updated_post = Note.objects.get(id=1)
        # Check if the title and content were updated correctly
        self.assertEqual(updated_post.title, 'Updated Test Note')
        self.assertEqual(updated_post.content, 'This is an updated test note.')


class NoteViewTest(TestCase):
    def setUp(self):
        # Create a Note object for testing views
        Note.objects.create(
            title='Test Note',
            content='This is a test note.',
        )

    def test_note_list_view(self):
        # Test the note-list view
        response = self.client.get(reverse('note_list'))
        # Check if the response is successful
        self.assertEqual(response.status_code, 200)
        # Check if the response contains the note's title
        self.assertContains(response, 'Test Note')

    def test_note_detail_view(self):
        # Test the note-detail view
        note = Note.objects.get(id=1)
        # Use reverse to get the URL for the note detail view
        response = self.client.get(reverse('note_detail', args=[str(note.id)]))
        # Check if the response is successful
        self.assertEqual(response.status_code, 200)
        # Check if the response contains the note's title and content
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'This is a test note.')

    def test_note_create_view(self):
        # Test the note-create view
        response = self.client.post(reverse('note_create'), {
            'title': 'New Note',
            'content': 'This is a new note.',
        })
        # Check if the response is a redirect
        self.assertEqual(response.status_code, 302)
        # Check if the new note was created
        self.assertTrue(Note.objects.filter(title='New Note').exists())

    def test_note_update_view(self):
        # Test the note-update view
        note = Note.objects.get(id=1)
        response = self.client.post(
            reverse('note_update', args=[str(note.id)]),
            {
                'title': 'Updated Note',
                'content': 'This is an updated note.',
            }
        )
        # Check if the response is a redirect
        self.assertEqual(response.status_code, 302)
        # Check if the note was updated
        updated_note = Note.objects.get(id=1)
        self.assertEqual(updated_note.title, 'Updated Note')
        self.assertEqual(updated_note.content, 'This is an updated note.')
