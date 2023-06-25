# Gym Scheduler

## Goal

The goal of this project is to develop a professional web application that enables gym members to efficiently schedule their workouts in a gym with limited space. The application should automate the scheduling process while allowing administrators to intervene manually when necessary.

## Requirements

1. **User Registration and Authentication:** Users should be able to register for an account, log in, and log out. The user's account should store their name, email, and password for authentication purposes. The authentication system we have chosen for this project is Django's simpleJWT.

1. **User Roles:** Two types of users should exist: regular users and administrators. Administrators should have the ability to manually intervene in the scheduling process through a simple web interface. Regular users should not have access to this interface.

3. **Membership Types:** Users can have regular or premium memberships. The type of membership affects the number of available slots for booking.

4. **Booking System:** Users should be able to choose a time slot for a workout through a simple web interface similar to google calendar. They availability of the time slot should be automaticly ditermined by the schdualing system. The system should also allow users to cancel or modify their bookings (up two hours before the schduled workout). Users shoul be able to see their schduled workouts in a calendar view and get notifications when their bookings are modified or deleted.

1. **Admin Intervention:** Administrators should have the capability to manually intervene in the scheduling process at any point and in any way trhourg an intuitive web interface. When conflicts arise, administrators should be notified and be able to resolve them by modifying or deleting existing bookings. Administrators should also be able to manually create bookings for users. 

6. **Operating Hours and Days:** The gym operates for 8 hours a day, 6 days a week. The booking system should consider these operating hours and days and only allow bookings during these times.

7. **Automated Scheduling:** The primary objective of the application is to automate as much of the scheduling process as possible. When a user requests a timeslot, the application should automatically determine whether the slot is available and book it if possible. If the slot is unavailable, the application should sugest 3 alternatives and if none of them is satisfactory, the user should be able to request a manual intervention from an administrator.

1. **Technology Stack:** The application will be built using Python, with Django as the primary web framework. At first it will be a RESTful API and later on a frontend will be added. The database will be SQLite. The application will be deployed to a server using Docker and Docker Compose. The frontend will be built using React. 

## Project Roadmap

Follow these steps to set up the project:

1. **Database Models:** Design the database models for each app. For example, in the "users" app, define a User model with fields for the user's name, email, password, role, and membership type. Consider extending Django's existing User model to leverage its built-in functionality.

2. **Migrations:** Create and apply database migrations to propagate model changes to the database schema. Use the command `python manage.py makemigrations app_name` to generate migrations for each app, and then apply them with `python manage.py migrate`.

3. **Views:** Define views as Python functions that handle web requests and return responses. Each app should have a views.py file where you define these views.

4. **URL Routing:** Set up URL routing for each app by creating a urls.py file in its directory. Associate each URL with a specific view. Don't forget to include these URLs in the project's main urls.py file.

5. **Templates:** If your views return HTML, create templates to simplify the generation of these HTML files. Store the templates in a templates directory within each app's directory.

6. **Admin Interface:** Django provides a built-in admin interface for managing app data. Register your models in each app's admin.py file to make them accessible in the admin interface.

7. **User Authentication:** Utilize Django's built-in user authentication system for user registration, login, and logout functionalities.

8. **Static and Media Files:** Create a static directory within each app to store static files like CSS, JavaScript, and images. For user-uploaded files, set up a media directory in your project.

9. **Testing:** Take advantage of Django's built-in testing framework to write unit tests for your views, models, and other components.

10. **Deployment:** Once your application is ready, deploy it to a server to make it accessible on the internet.



Remember the DRY principle (Don't Repeat Yourself) while working with Django. The framework aims to automate and reuse components whenever possible. Always explore Django's built-in features and third-party packages before reinventing the wheel.


# RESTful API

Yes, you can use Django REST Framework to build this project as a RESTful API. Django REST Framework is a powerful and flexible toolkit for building Web APIs in Django, and it is perfectly suited to handle the requirements of this project. Here's a high-level roadmap for how you might implement this using Django REST Framework:

## User Registration and Authentication
Django REST Framework works seamlessly with Django's built-in User model. You can utilize Django's built-in authentication system or Django REST Framework's token-based authentication for user registration, login, and logout.

## User Roles
You can extend Django's User model to include a role field. This field would indicate whether a user is a regular user or an administrator. Django's built-in permissions and groups can also be used to manage user roles and permissions.

## Membership Types
Similar to user roles, you can extend the User model to include a membership type field. This field would indicate whether a user is a regular or premium member. You can then use this field to manage the number of available booking slots for each user.

## Booking System
You can create a Booking model to manage bookings. The model would include fields such as user (a foreign key to the User model), time slot, and status. Django REST Framework can then be used to create a booking API that includes operations like create (book a slot), retrieve (check booking status), update (modify a booking), and delete (cancel a booking).

## Admin Intervention
Django REST Framework provides built-in support for Django's admin interface. Administrators can use the admin interface to manually intervene in the scheduling process as needed.

## Operating Hours and Days
You can create a Gym model that includes fields for operating hours and days. The booking API can then check these fields to ensure bookings are only made during operating hours.

## Automated Scheduling
You can use Django's built-in support for custom management commands to automate tasks such as deleting past bookings at the end of the day. These commands can then be run automatically using a task scheduler like cron.

## Technology Stack
Django REST Framework is built for Django and Python, so it fits perfectly into this technology stack. For the frontend, you could use a JavaScript framework like React, Angular, or Vue.js to consume the API. Django also supports a variety of databases, including PostgreSQL, MySQL, SQLite, and Oracle.

## Testing
Django REST Framework provides support for writing unit tests for your API. You can use Django's built-in testing framework to write tests for your views, models, and other components.

## Deployment
Once your application is ready, you can deploy it to a server. Django is compatible with many popular web servers, including Apache and Nginx. For ease of deployment, you might consider using a platform like Heroku, AWS, or Google Cloud Platform.

Remember to follow best practices when designing your API, including using the correct HTTP verbs for different actions (GET, POST, PUT, DELETE, etc.), handling errors properly, and versioning your API to allow for changes over time. And as always, make sure to secure your API to protect sensitive user data and prevent unauthorized access.
