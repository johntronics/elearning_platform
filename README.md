# CM3035 Final Coursework: Asynchronous eLearning Platform

## Overview
This project is an advanced eLearning platform built with Django, demonstrating modern web development practices including real-time bi-directional communication and asynchronous background task processing.

### Key Architectural Features:
* **Real-Time Chat:** Implemented using ASGI, WebSockets, and Django Channels (utilizing the `InMemoryChannelLayer` for local environment stability) to allow instant messaging between students and teachers.
* **Background Tasks:** Integrates Celery and a native Redis message broker to offload heavy processes, specifically generating email notifications when course materials are uploaded.
* **RESTful API:** Utilizes Django REST Framework (DRF) ViewSets and Routers to expose course and user data safely.

---

## Prerequisites
To run this project locally, ensure you have the following installed:
* Python 3.10+
* Redis Server (Native OS installation required for Celery broker)

---

## Installation & Setup

**1. Clone/Extract the repository and navigate into the project directory:**
cd elearning_platform

**2. Create and activate a virtual environment:**
(Windows)
python -m venv venv

venv\Scripts\activate

(macOS/Linux)
python3 -m venv venv

source venv/bin/activate

**3. Install the required dependencies:**
pip install -r requirements.txt

**4. Apply database migrations:**
python manage.py migrate

---

## Running the Application

Because this application utilizes background workers and asynchronous features, **three separate terminal windows** are required to run the full suite of features.

**Terminal 1: Start the Redis Server**
You can run redis via docker(docker run -p 6379:6379 -d redis)

Ensure Redis is running in the background to handle the Celery task queue:
redis-server --daemonize yes

*(Note: You can verify Redis is running by typing `redis-cli ping`. It should return `PONG`.)*

**Terminal 2: Start the Celery Worker**
With your virtual environment activated, start the Celery worker to listen for material upload events:
celery -A elearning_platform worker -l info

**Terminal 3: Start the Django ASGI Server**
With your virtual environment activated, start the main web server:
python manage.py runserver

You can now access the application at: http://127.0.0.1:8000/

---

## Test Credentials
To evaluate the platform, you can use the following pre-configured accounts:

**Teacher Account**
* **Username:** JohnTronics
* **Password:** testteacher1

**Student Account**
* **Username:** LP
* **Password:** testdent2