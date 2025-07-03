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

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download local static files (Important):**
    The `base.html` template has been updated to reference local copies of Bootstrap, Font Awesome, and jQuery. You will need to download these manually and place them in the correct `static/simplesocial/vendor/` subdirectories:
    *   **Bootstrap v4.1.3 CSS & JS:**
        *   Download from [https://getbootstrap.com/docs/4.1/getting-started/download/](https://getbootstrap.com/docs/4.1/getting-started/download/) (Compiled CSS and JS)
        *   Place `bootstrap.min.css` in `static/simplesocial/vendor/bootstrap/css/`
        *   Place `bootstrap.bundle.min.js` (which includes Popper.js) in `static/simplesocial/vendor/bootstrap/js/`. If you download `bootstrap.min.js` without Popper.js, you'll also need `popper.min.js` in the same directory.
    *   **Font Awesome v4.7.0 CSS:**
        *   Download from [https://fontawesome.com/v4.7.0/get-started/](https://fontawesome.com/v4.7.0/get-started/) (select the "Download" option, not CDN)
        *   Extract and place `font-awesome.min.css` in `static/simplesocial/vendor/font-awesome/css/`
        *   You will also need the `fonts` directory from the Font Awesome download. Place it in `static/simplesocial/vendor/font-awesome/` (so you'll have `static/simplesocial/vendor/font-awesome/css/font-awesome.min.css` and `static/simplesocial/vendor/font-awesome/fonts/...`).
    *   **jQuery v3.3.1 Slim:**
        *   Download from [https://jquery.com/download/](https://jquery.com/download/) (slim minified version)
        *   Place `jquery.slim.min.js` in `static/simplesocial/vendor/jquery/`

    Your `static/simplesocial/vendor/` directory should look something like this:
    ```
    static/
    └── simplesocial/
        └── vendor/
            ├── bootstrap/
            │   ├── css/
            │   │   └── bootstrap.min.css
            │   └── js/
            │       └── bootstrap.bundle.min.js  (or bootstrap.min.js + popper.min.js)
            ├── font-awesome/
            │   ├── css/
            │   │   └── font-awesome.min.css
            │   └── fonts/
            │       ├── FontAwesome.otf
            │       ├── fontawesome-webfont.eot
            │       ├── fontawesome-webfont.svg
            │       ├── fontawesome-webfont.ttf
            │       └── fontawesome-webfont.woff
            │       └── fontawesome-webfont.woff2
            └── jquery/
                └── jquery.slim.min.js
    ```

5.  **Set up Environment Variables (Optional but Recommended for Production):**
    *   **SECRET_KEY:** For production, it's crucial to set the `DJANGO_SECRET_KEY` environment variable to a strong, unique secret. The application will use a default key if this is not set, which is insecure for production.
    ```bash
    export DJANGO_SECRET_KEY='your_strong_secret_key_here'
    ```

6.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

7.  **Create a superuser (optional, for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

8.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`.

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
