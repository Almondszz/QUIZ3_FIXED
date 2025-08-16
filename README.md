# Job Portal Django Project

A simple job portal built with Django, supporting job posting, image uploads, user registration and authentication.

---

## Features

- User registration and login
- Job listing and search
- Create job postings with image upload
- Bootstrap-styled UI

---

## Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)
- [Git](https://git-scm.com/)
- (Recommended) [virtualenv](https://virtualenv.pypa.io/en/latest/)

---

## Setup Instructions

### 1. **Clone the Repository**

```bash
git clone https://github.com/Almondszz/QUIZ3_FIXED.git
cd <QUIZ3_FIXED>
```

### 2. **Create and Activate Virtual Environment**

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. **Install Python Packages**

```bash
pip install -r requirements.txt
```
> If `requirements.txt` does not exist, manually install Django:
> ```bash
> pip install django
> ```

### 4. **Apply Database Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. **Create a Superuser (Admin Account)**

```bash
python manage.py createsuperuser
```
Follow the prompts to set up username and password.

### 6. **Collect Static Files (for production use)**

```bash
python manage.py collectstatic
```

---

## Running The Server

Start the Django development server:

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.

---

## Media and Static Files

- **Static files** (e.g., Bootstrap) are served from the `static/` directory.
- **Uploaded images** are stored in the `media/` directory.

Ensure your `settings.py` includes:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

And your main `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your urls ...
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## Bootstrap Setup

Bootstrap is included via the `static/bootstrap/` directory or CDN.  
If using local files, verify the Bootstrap files exist at `static/bootstrap/css/bootstrap.min.css` and `static/bootstrap/js/bootstrap.bundle.min.js`.

---

## Admin Panel

You can log in at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) using the superuser credentials.

---

## Customization

- Edit templates in the `templates/` directory to customize UI.
- Modify models in `jobs/models.py` to change job fields.

---

## Troubleshooting

- If you see errors about missing static or media files, double-check directory structure and settings.
- If you can't log in, ensure your superuser credentials are correct.
- For further issues, check the Django documentation: https://docs.djangoproject.com/

---

## License

MIT (or your license of choice).

---

## Credits

Built using [Django](https://www.djangoproject.com/) and [Bootstrap](https://getbootstrap.com/).