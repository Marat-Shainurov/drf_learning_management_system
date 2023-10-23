# General description
drf_lms is a django-rest-framework project. \
The project is a backend part of the learning management system.
Main stack: Djangorestframework, Postgresql, Redis, Celery, django-celery-beat, Stripe.

# Install and usage
1. Clone the project from https://github.com/Marat-Shainurov/drf_learning_management_system to your local machine.

2. Build a new image and run the project container from the root project directory:
   - docker-compose build
   - docker-compose up

3. Read the project's documentation (swagger or redoc format):
   - http://127.0.0.1:8000/swagger/
   - http://127.0.0.1:8000/redoc/

4. Go to the main page on your browser http://127.0.0.1:8000/ and start working with the app's endpoints.

# Fixture
You can load the fixture with several testing objects:
  - docker-compose exec app_sales_networks python manage.py loaddata fixture_lms.json
  - Credentials: 
    {
      "email": "test@mail.com",
      "password": "123"
    }

# Project structure and models
1. *courses* - courses app.
   - *Course* - course model. 
   - *Lesson* - lesson model.\
     Related to Course via ForeignKey.
   - *Payment* - payment model.
     Related to both Course and Lesson models via Foreign Key.\
     Either paid_course or paid_lesson must be selected.\
     Two types are allowed - 'cash' or 'transfer'.
   - *Subscription* - subscription to a course model.
     Related to Course via Foreign Key.

2. *users* - users app.
   - User - customized User model.
   - UersManager class is overridden and customized (./users/manager.py)
   - Admin interface is overridden and customized. (./users/admin.py)

# Integrations
- Integration with Stripe API has been configured to simulate the payment process.
- All the stripe objects (product, price, session) are created for the Payment model objects.
- The Stripe API documentation https://stripe.com/docs/api

# Testing
- All the endpoints are covered by pytest tests in <app>/tests/
- Run tests:\
  docker-compose exec app python manage.py test

