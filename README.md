# PG Finder

A Django-based web application for browsing and booking PG (Paying Guest) accommodations across multiple cities. Users can explore available flats by city, view detailed listings with amenities and images, and book a stay directly through the platform.

Features
City-wise browsing — View available PG listings filtered by city (Mumbai, Pune, Bangalore, Chennai)
Detailed flat listings — Each listing includes images, BHK type, gender preference, amenities, and address details
User authentication — Custom signup, login, and logout functionality with extended user profiles (phone number, gender)
Booking system — Registered users can book a PG, providing personal and guardian contact details, check-in/check-out dates, and payment mode
Booking history — Users can view their past and current bookings
Feedback system — Visitors can submit feedback and satisfaction ratings
Amenities management — Flats are linked to multiple amenities via a many-to-many relationship
Tech Stack
Backend: Python, Django
Database: SQLite (development) — Django ORM for all data modeling
Frontend: HTML, CSS (Django templates)
Authentication: Django's built-in auth system, extended with a custom us
