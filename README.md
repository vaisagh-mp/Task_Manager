
# Task Manager

A simple task management web application built with Django, allowing users to create, update, delete, and filter tasks, with sorting and searching features.

## How to Run the Program

### 1. Clone the Repository

```bash
git clone <repository_url>
cd task_manager
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

If you don’t have a virtual environment, create one with:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

### 3. Install Required Dependencies

Install the required packages by running:

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

Make sure your database schema is up to date by running:

```bash
python manage.py migrate
```


### 5. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Now, you can access the application at `http://127.0.0.1:8000/`.

## Additional Features

### Task Management Features:
- **Create a Task**: Add new tasks by providing a description, deadline, status, and priority.
- **Update a Task**: Edit existing task details (description, deadline, status, priority).
- **Delete a Task**: Remove a task from the system.
- **Search Tasks**: Use the search bar to filter tasks by description.
- **Sort Tasks**: Sort tasks by deadline, status, or priority.

### Task Filtering:
- **View Pending Tasks**: View tasks with a status of "pending".
- **View Completed Tasks**: View tasks with a status of "completed".

### Task Due Alerts:
- **Due Soon**: Tasks with a deadline within 1 day will be highlighted with a "Due Soon!" alert next to their details.

## Assumptions & Design Decisions

- **Database**: The application uses SQLite by default. You can configure it to use PostgreSQL or MySQL by adjusting the `DATABASES` settings in `settings.py`.
- **Form Handling**: Django's `ModelForm` is used to handle task creation and updating.
- **Frontend Design**: The user interface is simple and straightforward using basic HTML and CSS.
- **Task Status**: Task status can be either `pending` or `completed`. You can add or modify the choices if needed.
- **Task Priorities**: Tasks are classified into `high`, `medium`, and `low` priority. You can modify these priority levels based on your needs.

