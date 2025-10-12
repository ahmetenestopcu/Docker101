# Docker101
An explanatory and comprehensive guide for those who don't know what docker and containers are.

## What is Docker?

Docker is a platform that allows you to package and run applications in isolated environments called containers. Containers include everything your application needs to run: code, runtime, system tools, libraries, and settings.

## Project Overview

This project demonstrates a simple Flask web application running inside a Docker container. The app displays "Hello from a Docker Container! 🐳" when accessed.

## Project Files

- **app.py**: A simple Flask web application
- **requirements.txt**: Python dependencies (Flask)
- **Dockerfile**: Instructions to build the Docker image

## Prerequisites

- Docker installed on your system ([Download Docker](https://www.docker.com/get-started))

## Step-by-Step Guide

### Step 1: Understanding the Flask Application

The `app.py` file contains a simple Flask web server that:
- Creates a Flask application
- Defines a route for the home page (`/`)
- Returns the message "Hello from a Docker Container! 🐳"
- Runs on host `0.0.0.0` and port `5000` (accessible from outside the container)

### Step 2: Understanding the Requirements File

The `requirements.txt` file lists all Python packages needed:
- Flask: The web framework for our application

### Step 3: Understanding the Dockerfile

The Dockerfile contains instructions to build our Docker image:
- **FROM python:3.9-slim**: Uses Python 3.9 slim version as the base image
- **WORKDIR /app**: Sets the working directory inside the container to `/app`
- **COPY requirements.txt .**: Copies the requirements file first (for better caching)
- **RUN pip install -r requirements.txt**: Installs Python dependencies
- **COPY . .**: Copies all application code into the container
- **EXPOSE 5000**: Documents that the container listens on port 5000
- **CMD ["python", "app.py"]**: Runs the Flask application when the container starts

### Step 4: Build the Docker Image

Open a terminal in the project directory and run:

```bash
docker build -t flask-docker-app .
```

This command:
- `docker build`: Builds a Docker image
- `-t flask-docker-app`: Tags the image with the name "flask-docker-app"
- `.`: Uses the Dockerfile in the current directory

### Step 5: Run the Docker Container

After building the image, run the container:

```bash
docker run -p 5000:5000 flask-docker-app
```

This command:
- `docker run`: Creates and starts a new container
- `-p 5000:5000`: Maps port 5000 on your host to port 5000 in the container
- `flask-docker-app`: The name of the image to use

### Step 6: Access the Application

Open your web browser and navigate to:

```
http://localhost:5000
```

You should see: **Hello from a Docker Container! 🐳**

### Step 7: Stop the Container

To stop the running container:
1. Press `Ctrl + C` in the terminal where the container is running

Or, in a new terminal:
```bash
docker ps                    # List running containers
docker stop <container-id>   # Stop the container
```

## Useful Docker Commands

### List all Docker images:
```bash
docker images
```

### List running containers:
```bash
docker ps
```

### List all containers (including stopped):
```bash
docker ps -a
```

### Remove a container:
```bash
docker rm <container-id>
```

### Remove an image:
```bash
docker rmi <image-name>
```

### Run container in detached mode (background):
```bash
docker run -d -p 5000:5000 flask-docker-app
```

### View container logs:
```bash
docker logs <container-id>
```

## Key Concepts

- **Container**: A lightweight, standalone package that includes everything needed to run the application
- **Image**: A template used to create containers
- **Dockerfile**: A text file with instructions to build a Docker image
- **Port Mapping**: Connects a port on your host machine to a port in the container
- **Layer Caching**: Docker caches each layer of the image build process for efficiency

## Benefits of Using Docker

1. **Consistency**: "It works on my machine" problem solved
2. **Isolation**: Applications run in isolated environments
3. **Portability**: Run anywhere Docker is installed
4. **Efficiency**: Lightweight compared to virtual machines
5. **Scalability**: Easy to scale applications up or down

## Next Steps

- Explore Docker Compose for multi-container applications
- Learn about Docker volumes for data persistence
- Study Docker networking for container communication
- Explore container orchestration with Kubernetes

## License

This project is open source and available for educational purposes.
