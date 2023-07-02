# Gym Scheduler

![Project Logo](logo_link)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

Gym Scheduler is a robust and efficient gym scheduling application built with Django and Django Rest Framework. The application is designed to manage gym schedules, user bookings, and user management. It provides a simple and intuitive API for managing gym schedules and bookings.

## Features

- ### User Management
    
    The users app has the following characteristics:
    
    #### User Model
    
    The user model is a custom model that extends Django's `AbstractBaseUser` and `PermissionsMixin`. It includes fields for email (which is used as the username field), name, is_active, is_staff, is_admin, and membership_type. The `membership_type` field is a choice field with options for 'Regular' and 'Premium' membership.
    
    #### User Manager
    
    The user manager is a custom manager that includes methods for creating a user and creating a superuser. The `create_user` method normalizes the email, sets the password, and saves the user. The `create_superuser` method sets the `is_staff` and `is_superuser` fields to True and then calls the `create_user` method.
    
    #### Views
    
    The views include `UserRegistrationView`, `UserLoginView`, and `UserLogoutView`. `UserRegistrationView` handles user registration and returns a JWT token upon successful registration. `UserLoginView` handles user login and returns a JWT token upon successful login. `UserLogoutView` handles user logout and blacklists the provided refresh token.
    
    #### Permissions
    
    The `IsUnauthenticated` permission class is used to ensure that only unauthenticated users can access certain views. This permission is used in the `UserRegistrationView` and `UserLoginView` to prevent authenticated users from accessing these views.
    
    #### Serializers
    
    The `UserSerializer` is used to serialize the user model. The `UserRegistrationSerializer` is used to validate user registration data. The `UserLoginSerializer` is used to validate user login data.

- ### Schedule Management: 
    - Gym Scheduler allows the creation of time-slots for each day of the week by the staff. Each time-slot has a specified start time, end time, the number of regular and premium available bookings and a list of gym staff that will be pressent at the time. The application ensures that:
        - The user is authenticated.
        - The user is a gym staff.
        - The staff can create an arbitrary nuber of slots and manage their characteristics.
        - The staff can delete any of the slots.
        - The staff can update any of the slots.
        - The staff can view all the slots.
        - The staff can view all the bookings for a specific slot.
        - The staff can view all the bookings for a specific time period.
        - The staff can view all the bookings for a specific user.

- ### Booking Management: 
    - Users can request to book any of the available slots. The application ensures that:
        - The user is authenticated.
        - The user has not already booked more than one additional slot for the same day.
        - The user has not already booked a slot for the same time.
        - The slot is not already fully booked.
        - The user is a premium member if the slot is premium-only.
    - If all the above conditions are met:
        - The booking is created
        - The user is notified in the response 
        - An email containing a google calendar invite with the booking details is sent to the user
    - Otherwise:
        - The user is notified of the reason for the failure
        - The user has the ability to notify an administrator of the issue.

## Installation

Please follow the instructions below to set up the project locally.

```bash
# Clone the repository
git clone https://github.com/orestis42/gym_scheduler.git

# Navigate into the directory
cd gym_scheduler

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
```
## Usage

The application provides a simple API for managing gym schedules and bookings. The API documentation can be found [here]().

