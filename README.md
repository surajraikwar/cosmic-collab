# Star Social - Django Social Media Project

Star Social is a social media platform built with Python and Django, based on the "Python and Django Full Stack Web Developer Bootcamp" Udemy course. This project allows users to create accounts, join groups, create posts, and interact with other users.

## Project Overview

This project was originally created as part of a Udemy course and has been updated to use more recent versions of Django and other dependencies. It serves as a demonstration of building a full-stack web application with Django.

## Features

*   User authentication (signup, login, logout)
*   User profiles
*   Groups:
    *   Create and join groups
    *   View group details and members
    *   Post messages within groups
*   Posts:
    *   Create posts within groups or for all users
    *   View posts from users and groups
    *   Delete user's own posts
*   Interactive "firefly" background animation on the homepage.

## Tech Stack

*   Python 3.10+
*   Django 5.2.4
*   django-bootstrap4 25.1 (for Bootstrap 4 integration)
*   misaka 2.1.1 (for Markdown processing)
*   django-braces 1.17.0 (for utility mixins)
*   SQLite (default database)
*   HTML, CSS, JavaScript
*   Bootstrap 4.1.3 (CSS framework)
*   Font Awesome 4.7.0 (icons)
*   jQuery 3.3.1 (JavaScript library for Bootstrap 4)

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/surajraikwar/starsocial.git
   cd starsocial
   ```

2. **Set up a virtual environment**
   ```bash
   # Create a virtual environment
   python -m venv venv
   
   # Activate the virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   # venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up static files**
   ```bash
   # Create necessary directories
   mkdir -p static/simplesocial/vendor/{bootstrap/{css,js},font-awesome/{css,fonts},jquery}
   
   # Download and place static files (or copy from existing project)
   # Bootstrap 4.1.3
   # - Download from: https://getbootstrap.com/docs/4.1/getting-started/download/
   # - Place bootstrap.min.css in static/simplesocial/vendor/bootstrap/css/
   # - Place bootstrap.bundle.min.js in static/simplesocial/vendor/bootstrap/js/
   
   # Font Awesome 4.7.0
   # - Download from: https://fontawesome.com/v4.7.0/get-started/
   # - Extract and place font-awesome.min.css in static/simplesocial/vendor/font-awesome/css/
   # - Copy the fonts/ directory to static/simplesocial/vendor/font-awesome/
   
   # jQuery 3.3.1
   # - Download from: https://jquery.com/download/ (slim minified version)
   # - Place jquery.slim.min.js in static/simplesocial/vendor/jquery/
   ```

5. **Set up environment variables** (recommended for production)
   ```bash
   # Create a .env file in the project root
   echo "DJANGO_SECRET_KEY=your-secret-key-here" > .env
   
   # Generate a secure key with:
   # python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```

### Running the Application

1. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

2. **Create a superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

3. **Start the development server**
   ```bash
   python manage.py runserver
   ```

4. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin interface: http://127.0.0.1:8000/admin/

### Development Commands

- Run tests: `python manage.py test`
- Create new migrations: `python manage.py makemigrations`
- Apply migrations: `python manage.py migrate`
- Collect static files: `python manage.py collectstatic`

### Project Structure
```
starsocial/
├── accounts/           # User authentication app
├── groups/            # Groups functionality
├── posts/             # Posts functionality
├── simplesocial/      # Project settings
├── static/            # Static files (CSS, JS, images)
│   └── simplesocial/
│       ├── css/       # Custom CSS
│       ├── js/        # JavaScript files
│       └── vendor/    # Third-party libraries
├── templates/         # HTML templates
├── manage.py          # Django management script
└── requirements.txt   # Project dependencies
```

## Project Structure

*   `simplesocial/`: Main project directory.
    *   `settings.py`: Django project settings.
    *   `urls.py`: Project-level URL configurations.
*   `accounts/`: Django app for user accounts and authentication.
*   `groups/`: Django app for managing groups.
*   `posts/`: Django app for managing posts.
*   `static/`: Static files (CSS, JavaScript, images).
    *   `simplesocial/css/master.css`: Custom global CSS.
    *   `simplesocial/js/master.js`: Custom JavaScript for homepage animation.
    *   `simplesocial/vendor/`: Directory for third-party static assets (Bootstrap, Font Awesome, jQuery).
*   `templates/`: Project-level HTML templates.
    *   `base.html`: Base template inherited by other templates.
    *   `index.html`: Homepage template.
*   `manage.py`: Django's command-line utility.
*   `requirements.txt`: Python dependencies.
*   `db.sqlite3`: SQLite database file.

## Backend Improvements Made

*   Upgraded Django from 2.0.5 to 5.2.4.
*   Upgraded `django-bootstrap4` to the latest compatible version (25.1).
*   Added missing dependencies (`misaka`, `django-braces`) to `requirements.txt`.
*   Set `DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'` in `settings.py` to use modern auto-incrementing primary keys.
*   Updated `SECRET_KEY` in `settings.py` to be loaded from an environment variable (`DJANGO_SECRET_KEY`) with a fallback for development, enhancing security.
*   Added a comment in `settings.py` to remind developers to set `DEBUG = False` in production environments.

## Frontend Improvements Made

*   Updated `templates/base.html` to load Bootstrap, Font Awesome, and jQuery from local static files instead of CDNs. This requires manually downloading these assets (see Setup section).
*   Changed the navbar class from `bg-black` (custom) to `bg-dark` (standard Bootstrap) in `templates/base.html` for better Bootstrap integration.

## Potential Future Improvements

*   **Upgrade to Bootstrap 5:** Modernize the UI further by upgrading from Bootstrap 4 to Bootstrap 5. This would involve updating HTML templates for new class names and potentially refactoring JavaScript that relies on Bootstrap's jQuery plugins.
*   **Comprehensive Testing:** Add more unit and integration tests to ensure code quality and prevent regressions.
*   **User Profile Enhancements:** Allow users to add more information to their profiles (e.g., avatar, bio).
*   **AJAX for Interactions:** Use AJAX for actions like joining/leaving groups or liking posts to improve user experience.
*   **Deployment Configuration:** Add configurations and instructions for deploying to platforms like Heroku, PythonAnywhere, or AWS.
*   **Replace Misaka:** `misaka` is a Markdown parser. Consider replacing it with a more actively maintained library like `markdown2` or `CommonMark-py` if needed, and update any related code.
*   **Static File Management for Production:** Implement a more robust static file serving strategy for production (e.g., using WhiteNoise or collecting static files to a CDN).

## Troubleshooting

*   **`ModuleNotFoundError` for `distutils` during `python manage.py migrate` (older Python/Django versions):**
    This can happen with newer Python versions where `distutils` is removed. Installing `setuptools` usually resolves this: `pip install setuptools`. This project has been upgraded, so this should no longer be an issue.
*   **`AttributeError: module 'collections' has no attribute 'Iterator'`:**
    This occurs when using an older Django version (like 2.x) with a newer Python version (like 3.10+). Upgrading Django (as done in this project) is the primary solution.
*   **Static files (CSS/JS) not loading:**
    *   Ensure you have run `python manage.py collectstatic` if `DEBUG` is `False` (though for development, `DEBUG = True` is typical and `collectstatic` is not strictly needed if `STATICFILES_DIRS` is set correctly).
    *   Double-check the paths in `templates/base.html` and ensure the static files (Bootstrap, Font Awesome, jQuery) have been downloaded and placed in the correct `static/simplesocial/vendor/` subdirectories as described in the Setup section.
    *   Verify `STATIC_URL` and `STATICFILES_DIRS` in `simplesocial/settings.py`.

## Contributing

This project is primarily a personal showcase. However, if you have suggestions or find issues, feel free to open an issue or submit a pull request.
