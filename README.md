# Sticky Notes App

A simple Django application for creating, editing, and managing sticky notes.

## Features

- Create, edit, and delete notes
- Responsive UI

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd django-sticky-notes
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```bash
    python manage.py migrate
    ```

4. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

- Access the app at `http://127.0.0.1:8000/`

## Project Structure

- `sticky_notes/` - Django app containing models, views, and templates
- `manage.py` - Django management script
