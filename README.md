# Internship Tracker

A Django web application to track your internship and job applications. Log applications, update their status, filter/search your list, and monitor stats like interview and offer rates.

---

## Features

- User authentication (signup, login, logout)
- Add, edit, and delete applications
- Dashboard analatics (total, interview rate, offer rate)
- Track status: Applied, Interview, Rejected, Offer
- Filter applications by status and search by company or role
- Paginated application list

---

## Tech Stack

Backend

- Python 3
- Django
- MySQL
- Django ORM (Aggregation, Filtering, Pagination)

Frontend

- HTML
- Bootstrap 5
- Custom CSS (static files)

---

## Architecture Overview

- accounts app → Authentication logic
- applications app → Core application tracking features
- User-based data ownership enforced using ForeignKey
- Secure CRUD operations with ownership validation

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/z-ABYa/tracker/
cd tracker
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate (macOS/Linux)
venv\Scripts\activate (Windows)
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Database

Create a new MySQL DB:
```sql
create database tracker;
use tracker;
```

Then change 'PASSWORD' and 'USER' in `settings.py` file:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tracker',
        'HOST': 'localhost',
        'USER': '<your_mysql_username>',
        'PASSWORD': '<your_mysql_password>',
    }
}
```

### 5. Create a Superuser (Optional)

To access the Django admin panel:

```bash
python manage.py createsuperuser
```

### 6. Apply Migrations

```bash
python manage.py migrate
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## Project Structure

```
tracker/
│
├── accounts/
├── applications/
├── templates/
├── tracker/
│   └── settings.py/
├── static/
│   └── css/
├── manage.py
├── requirements.txt
└── README.md
```

---