# Gym Scheduler

## Goal

The goal of this project is to develop a professional web application that enables gym members to efficiently schedule their workouts in a gym with limited space. The application should automate the scheduling process while allowing administrators to intervene manually when necessary.

## Requirements

1. **User Registration and Authentication:** Users should be able to register for an account, log in, and log out. The user's account should store their name, email, and password for authentication purposes.

2. **User Roles:** Two types of users should exist: regular users and administrators. Administrators should have the ability to manually intervene in the scheduling process.

3. **Membership Types:** Users can have regular or premium memberships. The type of membership affects the number of available slots for booking (6 slots per hour for regular members, 3 slots per hour for premium members).

4. **Booking System:** Users should be able to request a time slot for a workout. The system should check for slot availability before confirming the booking. If a slot is not available, the system should notify the user. Each user can book up to 2 timeslots a day and the gym can accomondate up to 6 regular and 3 premium users per timeslot.  

5. **Admin Intervention:** Administrators should have the capability to manually intervene in the scheduling process at any point and in any way.

6. **Operating Hours and Days:** The gym operates for 8 hours a day, 6 days a week. The booking system should consider these operating hours and days and only allow bookings during these times.

7. **Automated Scheduling:** The primary objective of the application is to automate as much of the scheduling process as possible. This could include automatically deleting past bookings at the end of the day or implementing other automated processes as required.

8. **Technology Stack:** The application will be built using Python, with Django as the primary web framework. Additional technologies, such as frontend frameworks and databases, can be utilized as needed.

## Project Setup

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