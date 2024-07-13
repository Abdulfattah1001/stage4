## SPECIAL NOTE The ngrok you see here is changing dynamically if I had to restart server

# Flask Messaging System with Celery and RabbitMQ

This project is a messaging system built using Flask for the web framework, Celery for task management, and RabbitMQ as the message broker. The application is served behind NGINX and uses NGROK to expose the endpoint for public access.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Running the Application](#running-the-application)
5. [Project Structure](#project-structure)
6. [Usage](#usage)
7. [Monitoring](#monitoring)
8. [License](#license)

## Prerequisites

- Python 3.x
- Flask
- Celery
- RabbitMQ
- NGINX
- NGROK

## Installation

### RabbitMQ

Install RabbitMQ on your server:

```bash
sudo apt-get update
sudo apt-get install rabbitmq-server
sudo systemctl enable rabbitmq-server
sudo systemctl start rabbitmq-server
```

### Python Dependencies

Create a virtual environment and install the required Python packages:

```bash
python3 -m venv venv
source venv/bin/activate
```

### NGINX

Install NGINX:

```bash
sudo apt-get install nginx
```

## Configuration

### RabbitMQ Management Plugin (Optional)

Enable the RabbitMQ management plugin for easier monitoring:

```bash
sudo rabbitmq-plugins enable rabbitmq_management
```

Access the management interface at `http://localhost:15672` (default login: guest/guest).

### NGINX Configuration

Copy the provided NGINX configuration file `nginx.conf` to `/etc/nginx/sites-available/your_project` and create a symlink to `/etc/nginx/sites-enabled/`.

```bash
sudo cp nginx.conf /etc/nginx/sites-available/flask_app
sudo ln -s /etc/nginx/sites-available/your_project /etc/nginx/sites-enabled/
sudo systemctl restart nginx
```

## Running the Application

### Celery Worker

Start the Celery worker:

```bash
celery -A app.celery worker --loglevel=info
```

### Gunicorn

Start the Flask application with Gunicorn:

```bash
gunicorn -c gunicorn_config.py app:app
```

## Project Structure

```
your_project/
│
├── app/
│   ├── __init__.py
│   ├── index.py
│   ├── tasks.py
│   └── celeryconfig.py
```

### Files Description

- **`app/init.py`**: Initializes the Flask app and integrates Celery.
- **`app/celeryconfig.py`**: Contains configuration for Flask and Celery.
- **`app/index.py`**: Entry point to run the Flask app.
- **`app/tasks.py`**: Contains Celery task definitions.

## Usage

### Sending a Email

To send a message, make a POST request to the `/` endpoint with `sendmail` and `email_addr` parameters:

```bash
curl -X POST http://yourdomain.com/ -d "sendmail=example@gmail.com"
```

The message will be processed asynchronously by Celery.

## Monitoring

### RabbitMQ Management Interface

Access the RabbitMQ management interface at `http://localhost:15672`.

Access Flower at `http://localhost:5555`.

## Using ngrok to expose the localhost for public access
After the installation of ngrok which can be found on the website [https://dashboard.ngrok.com/get-started/setup/linux?domainId=rd_2jBNyWZ3tT2kCOwFR9isIzmmVF4](ngrok configuration for linux)

``http http://127.0.0.1:80``

## License

This project is licensed under the MIT License.

---

Feel free to customize this documentation as per your project's specifics and requirements.