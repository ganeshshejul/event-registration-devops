# Event Registration App

A simple Flask web application for event registration, with Docker support and a Jenkins CI/CD pipeline.

## Features

- Event registration form with:
  - Name
  - Email
  - Phone number
  - Event selection (`Hackathon`, `Workshop`, `Seminar`)
- Registration confirmation message after submission
- Responsive UI with light/dark mode toggle
- Dockerized deployment
- Jenkins pipeline for build and run

## Tech Stack

- Python 3.10
- Flask 2.3.2
- HTML/CSS/JavaScript (Jinja template)
- Docker
- Jenkins

## Project Structure

```text
.
├── app.py
├── Dockerfile
├── jenkinsfile
├── requirements.txt
└── templates/
    └── index.html
```

## Run Locally

### 1) Clone the repository

```bash
git clone https://github.com/ganeshshejul/event-registration-devops.git
cd event-registration-devops
```

### 2) Create and activate virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Start the app

```bash
python app.py
```

Open your browser at:

```text
http://localhost:5000
```

## Run with Docker

### Build image

```bash
docker build -t event-app .
```

### Run container

```bash
docker run -d -p 5000:5000 --name event-container event-app
```

Open:

```text
http://localhost:5000
```

### Stop and remove container

```bash
docker stop event-container
docker rm event-container
```

## Jenkins Pipeline

The `jenkinsfile` contains three stages:

1. **Checkout** – pulls source from GitHub
2. **Build Image** – builds Docker image `event-app`
3. **Run Container** – stops/removes old container and runs a new one on port `5000`

## Notes

- Application listens on `0.0.0.0:5000`.
- Ensure Docker is installed and Jenkins has permission to run Docker commands.
- The app currently returns a simple success message and does not persist registrations to a database.
