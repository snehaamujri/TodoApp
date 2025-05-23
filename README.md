# TodoApp
A simple Django-based Todo application with user authentication and admin management.

## Features

- User Signup, Login, and Logout
- Create, view, and delete todo items
- Admin panel to manage users and todos (restricted to staff users)
  
### Prerequisites

- Python 3.8+
- Django 4.x
- Virtual environment recommended
#### To start

1. Clone the repository:

   ```bash
   git clone https://github.com/snehaamujri/TodoApp.git
   cd your-repo
2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  
3. Apply migrations:
 
    ```bash
    python manage.py migrate
 4. For admin - createsuperuser
    ```bash
    python manage.py createsuperuser
5. Run server
   ```bash
   python manage.py runserver
6. Links:
   Todo App
   
      ```bash
      http://localhost:8000/
   

  Django admin panel

      http://localhost:8000/admin/ 


    

