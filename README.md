# Contact Management

Contact Management - is a project that allows you to store and manage contact information. The project uses Django and the Django REST Framework to create an API that allows interaction with contact data.

## Content

- [Requirements](#requirements)
- [Installation](#installation)
- [Settings](#settings)
- [Usage](#usage)
- [Google OAuth2](#google-oauth2)
- [Restrict access by IP](#restrict-access-by-ip)


## Вимоги

- Python 3.8 or higher
- Django 4.1
- Django REST Framework
- SQLite (for local DB)

## Requirements

1. Clone the repository:

    ```bash
    git clone <URL_РЕПОЗИТОРІЮ>
    cd contact_management

2. Create and activate the virtual environment:
    python -m venv env
    source env/bin/activate  # For Linux/Mac
    env\Scripts\activate  # For Windows

3. Install the necessary packages:
    pip install -r requirements.txt

4. Apply database migrations:
    python manage.py migrate

5. Start the server:
    python manage.py runserver


## Settings

1. Edit the settings.py file to configure your options (secret key, database, allowed hosts, etc.).
2. Add your Google OAuth authentication credentials to settings.py.
3. Adjust your URLs in urls.py if needed.


## Using

1. Use the contact management API:
    - Create a new contact: POST /api/contacts/
    - View the list of contacts: GET /api/contacts/
    - View a specific contact: GET /api/contacts/{id}/
    - Update contact: PUT /api/contacts/{id}/
    - Deleting a contact: DELETE /api/contacts/{id}/

2. Token authentication:
    - Get the token: POST /api/token/ with username and password.
    - Add the token to the request header: Authorization: Token <your_token>.


## Google OAuth2

To use Google OAuth2 in your application:

1. Create a project in the Google Developer Console.
2. Configure OAuth 2.0 by obtaining the Client ID and Client Secret.
3. Add these values ​​to your settings.py:
    - SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '<your_client_id>'
    - SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '<your_client_secret>'
4. Configure REDIRECT_URLS to determine where users will be redirected after login.


## Restricting access by IP

1. Allowed regions:
    - Access to the API is allowed only for users from Ukraine (UA) and Poland (PL).
    - All other regions will be automatically blocked.
2. IP address geolocation:
    - A free geolocation service (for example, ipapi.co) is used to determine the geographic location of the IP address.
    - When a user makes a request to the API, the system automatically checks their IP address.
3. Request processing:
    - If the user's IP address does not belong to the allowed regions, the system returns a response with a status code of 403 (Forbidden) and an access denial message.
4. Important notes
    - Local requests (from address 127.0.0.1 or ::1) always get access.
    - Access will also be blocked in case of errors when receiving country data.