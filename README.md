Navigation Menu




**Shop Registration and Search API**
The Shop Registration and Search API is a Django-based RESTful web service that allows users to register shops and search for them based on geographical location. Users can input their latitude and longitude to retrieve a list of registered shops sorted by their proximity to the user's location, calculated using the Haversine formula.

**Features**

Shop Registration: Allows shop owners to register their shops with details including name, latitude, and longitude.
Distance-Based Search: Users can input their current geographical coordinates to find nearby shops sorted by distance.
API Documentation: Automatically generated API documentation using Swagger, providing a user-friendly interface for testing endpoints.


**Technologies Used**

Django: Web framework for building the API.
Django REST Framework: Toolkit for building Web APIs.
drf-yasg: For generating OpenAPI documentation.
Python: Programming language for backend logic.
PostgreSQL/MySQL: Database for storing shop information (replace with your database of choice).

**Installation Prerequisites**

Python 3.6 or higher
Django 3.2 or higher
Django REST Framework
drf-yasg
mysqlclient  #as I used mysql


**Step 1: Clone the Repository**

bash

git clone "https://github.com/rupashreesmagic/shop-registration-system" cd shop_registration

**Step 2: Create a Virtual Environment**

bash

python -m venv venv source venv/bin/activate # On Windows use venv\Scripts\activate

**Step 3: Install Requirements**

bash

pip install django djangorestframework mysqlclient drf-yasg

**Step 4: Configure Database**

Update the settings.py file to configure your database settings.

In project's settings.py file,

DATABASES = { 'default': { 'ENGINE': 'django.db.backends.postgresql', # or 'django.db.backends.mysql' 'NAME': 'your_database_name', 'USER': 'your_database_user', 'PASSWORD': 'your_password', 'HOST': 'localhost', 'PORT': '', } }

**Step 5: Apply Migrations**

bash

python manage.py makemigrations
python manage.py migrate

**Step 6: Create a Superuser**

To access the Django admin panel:

bash

python manage.py createsuperuser

**Step 7: Run the Development Server**

bash

python manage.py runserver

**Step 8: Access API Documentation**

Navigate to http://127.0.0.1:8000/swagger/ to view the Swagger-generated API documentation. API Endpoints

Register Shop

Endpoint: /register_shop/

Method: POST

Request Body:

json

{ "name": "Shop Name", "latitude": 40.7128, "longitude": -74.0060 }

Search Shops

Endpoint: /search_shop/

Method: GET

Query Parameters: user_latitude: User's latitude (float) user_longitude: User's longitude (float)

Example Request: /search_shop/?user_latitude=40.7128&user_longitude=-74.0060

Response:

json

{ "message": "Shops retrieved successfully.", "data": [ { "id": 1, "name": "Shop A", "latitude": 40.7306, "longitude": -73.9352 }, { "id": 2, "name": "Shop B", "latitude": 40.7120, "longitude": -74.0150 } ] }



For any inquiries, please reach out to:

Your Name: Rupashree Roy
Email:rupashreeroy2000@gmail.com
