# 🐳 Simple Dockerized Python Web App

This repository provides a minimal, easy-to-understand example of how to containerize a simple Python Flask web application using Docker.

It's a perfect starting point for learning the basic `build` and `run` workflows of Docker.

## 📁 File Structure

```
.
├── Dockerfile          # The recipe for building the Docker image
├── app.py              # The simple Flask web application
├── requirements.txt    # Python dependencies for the project
└── README.md           # This instruction file
```

##  Prerequisites

Before you begin, ensure you have **Docker** installed on your machine.

- [Download and install Docker Desktop](https://www.docker.com/products/docker-desktop/) (for Mac and Windows) or Docker Engine (for Linux).

## 🚀 How to Run This Project: A Step-by-Step Guide

Follow these steps to build and run the application on your own machine.

### Step 1: Clone the Repository

First, clone this repository to your local machine using Git.

```bash
# Replace YOUR_USERNAME/YOUR_REPOSITORY with your actual GitHub info
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

### Step 2: Navigate to the Project Directory

Open your terminal and move into the cloned project folder.

```bash
cd Docker101
```

### Step 3: Build the Docker Image

Run the following command in your terminal. This command reads the `Dockerfile` and builds your application's image.

- `-t` gives your image a name (a "tag"), which we'll call `my-python-app`.
- `.` tells Docker to look for the `Dockerfile` in the current directory.

```bash
docker build -t my-python-app -f DockerFile .
```

You will see output in your terminal as Docker executes each step in the `Dockerfile`.

### Step 4: Run the Docker Container

Now that the image is built, you can run it as a container.

```bash
docker run --rm -p 8080:5000 my-python-app
```

**What does this command do?**
- `docker run`: Creates and starts a new container.
- `-p 8080:5000`: This is the port mapping. It connects your computer's (the "host") port `8080` to the container's internal port `5000`. Our Flask app runs on port `5000` inside the container, and this makes it accessible from your machine.
- `my-python-app`: The name of the image to run.

### Step 5: Access the Application ✅

Everything should be running now! Open your web browser and navigate to the following address:

[http://localhost:8080](http://localhost:8080)

You should see the message: **"Hello from a Docker Container! 🐳"**.

### Step 6: Stopping and Cleaning Up

- To stop the container, go back to your terminal and press `CTRL + C`.
- To see all containers (including stopped ones), run:
  ```bash
  docker ps -a
  ```
- To permanently remove a container, use its ID from the command above:
  ```bash
  docker rm <CONTAINER_ID>
  ```
- To remove the image you built:
  ```bash
  docker rmi my-python-app
  ```
