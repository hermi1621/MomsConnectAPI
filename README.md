
# MomsConnectAPI

## Project Description
MomsConnectAPI is a simple social platform for moms to share posts, chat, and interact with each other. Users can register, login, create posts with optional images, and see posts from other users. The project is built using **Django** and includes static files (HTML, CSS, JS) for the frontend templates.

## Features Implemented So Far
- User registration and login/logout
- CRUD for posts (create posts with optional images)
- Home page showing all posts
- Basic static files setup (CSS and JS)
- Admin interface to manage users and posts


Admin Panel (Browser)

URL:http://127.0.0.1:8000/admin/

Method: POST

URL:http://127.0.0.1:8000/accounts/api/register/
{
    "username": "hermela",
    "email": "hermela@gmail.com",
    "password": "12qw"
}
API Login (Get Token)

Method: POST

URL:http://127.0.0.1:8000/accounts/api/login/
{
    "username": "hermela",
    "password": "12qw"
}
API Create Post

Method: POST

URL:http://127.0.0.1:8000/accounts/api/posts/
{
    "content": "This is my first post!",
    "image": null
}

python manage.py runserver

