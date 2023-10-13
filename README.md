# TodoList App with Django and MySQL

This is a simple TodoList web application built using the Django framework and MySQL database. It provides basic functionality for users to register, log in, manage tasks and events, edit and delete them, update their profile, and log out. This README will guide you through the installation and usage of the TodoList app.

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

## Features

- **User Authentication:**
  - Register an account with a unique username and password.
  - Log in to your account securely.

- **Task Management:**
  - Add new tasks.
  - Edit and update tasks.
  - Delete tasks.

- **Event Management:**
  - Add new events.
  - Edit and update events.
  - Delete events.

- **User Profile:**
  - Update your profile information.

- **User Logout:**
  - Log out from your account.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed.
- Django 3.x installed.
- MySQL database server.
- MySQL client for Python (`mysqlclient`).

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Benup211/Django_TodoApp.git
cd capstone
```

4. Install required Python packages:

```bash
pip install django
```

5. Configure the MySQL database settings in the `settings.py` file:

```python
# Replace these values with your MySQL database information
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'capstone_db',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',  # Change to your database host if necessary
        'PORT': '3306',  # Change to your database port if necessary
    }
}
```

6. Apply database migrations:

```bash
cd capstone #ls having manage.py
python manage.py makemigrations
python manage.py migrate
```

7. Create a superuser account to access the Django admin panel:

```bash
python manage.py createsuperuser #ls having manage.py
```

8. Start the development server:

```bash
python manage.py runserver #ls having manage.py
```

The TodoList app should now be running locally. You can access it by opening your web browser and navigating to `http://localhost:8000`.

## Usage

1. **Login:**
   - Click on the "Login" link.
   - Enter your username and password.
   - Click "Login."
   - Else Register

2. **Register:**
   - Open the application in your browser.
   - Click on the "Register" link in login.
   - Provide a unique username and password with name & email.
   - Click "Register."

3. **Tasks:**
   - To add a task, click "Add Task," provide task details, and click "Add task"
   - To edit or delete a task, navigate to the task and use the respective buttons.

4. **Events:**
   - To add an event, click "Add Event," provide event details, and click "Add Event"
   - To edit or delete an event, navigate to the event and use the respective buttons.

5. **User Profile:**
   - Click "Update Profile" to update your user information.

6. **Logout:**
   - Click "Logout" to log out of your account.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name.
3. Make your changes and commit them with clear messages.
4. Push your branch to your forked repository.
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---