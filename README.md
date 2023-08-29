# Exalens Sensor Challenge

## Overview

### Purpose

The purpose of this project is to simulate the behavior of IoT sensors, monitor their readings, and expose APIs to fetch sensor data based on specific criteria. This system uses MQTT for real-time data transfer, MongoDB for persistent data storage, Redis for in-memory caching, and FastAPI for API endpoints.



## 🌟 Features

-   **MQTT Broker**: Uses Mosquitto as an MQTT broker, encapsulated in a Docker container.
-   **MQTT Publisher and Subscriber**: Written in Python, for real-time data publishing and subscribing.
-   **Data Storage**: Utilizes MongoDB as a database for persistent data storage.
-   **In-Memory Cache**: Leverages Redis for fast in-memory data access.
-   **API Endpoints**: Developed using FastAPI, providing a well-documented and performant API.
-   **Container Orchestration**: Utilizes Docker Compose for easy service management.

----------

## 📦 Services in `docker-compose.yaml`

Here is a brief overview of the services defined in the `docker-compose.yaml` file:

-   `mosquitto`: MQTT broker for handling real-time messaging.
-   `mongo`: MongoDB database for storing sensor readings.
-   `redis`: Redis in-memory data store for caching and quick data retrieval.
-   `mqtt-publisher`: Python-based MQTT publisher service.
-   `mqtt-subscriber`: Python-based MQTT subscriber service.
-   `fastapi`: FastAPI application to serve API endpoints.

----------

## 🚀 Setup Instructions

### Clone the Repository

`git clone <repository_url>` 

### Navigate to the Project Directory

`cd <directory_name>` 

### Start Services with Docker Compose

`docker-compose up -d` 

This command starts all the services defined in `docker-compose.yaml` in detached mode.

### Check the Running Services

`docker-compose ps` 

### Access the FastAPI Documentation

Open your web browser and navigate to [FastAPI Documentation](http://localhost:8000/docs).

----------

## 📌 API Endpoints

### Get Sensor Readings by Date Range

Fetch sensor readings within a specific date range:

`GET /readings?start_datetime=<start_datetime>&end_datetime=<end_datetime>` 

### Get Last 10 Readings for a Sensor

Retrieve the last 10 sensor readings for a specific sensor:

`GET /latest-readings/{sensor_id}`

