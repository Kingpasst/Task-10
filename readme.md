```markdown
# NeedWeed

NeedWeed is a Web Store App that allows users to create and participate in polls. The application includes user authentication features, enabling users to register, log in, and manage their profiles.

## Features

- User registration and authentication (login/logout)
- Create, view, and manage polls
- Vote on polls and view results
- User profile management

## Technologies Used

- Django
- SQLite (default database)
- HTML/CSS for frontend
- Bootstrap for styling

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Kingpasst/Task-10.git
   cd Task-10
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Run database migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser (optional, for admin access):

   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

8. Access the application by visiting `http://127.0.0.1:8000/` in your web browser.

## Usage

- Visit the home page to view the latest polls.
- Register an account to create polls and vote.
- Log in to access your profile and manage your polls.
- Explore the polls and cast your votes.
