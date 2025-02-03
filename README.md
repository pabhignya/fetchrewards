# Fetch rewards Web Service

This project implements a Receipt Processor web service using Python and Docker, following the OpenAPI 3.0.3 specification. The service is designed to process receipts and calculate points.

## Overview

The web service exposes two APIs, both of which were implemented based on the instructions provided in the following link:

https://github.com/fetch-rewards/receipt-processor-challenge

The two APIs are:

1. **Receipt Upload API**: Allows users to upload receipts.
2. **Points Retrieval API**: Allows users to retrieve points of processed receipt data in JSON format.

## Features

- **OpenAPI 3.0.3 Specification**: The APIs are designed and implemented following the OpenAPI 3.0.3 standards.
- **JSON File Storage**: Receipt data is stored in JSON files for persistence.
- **Dockerized**: The entire service is containerized using Docker for easy deployment and scalability.

## Installation

### Prerequisites

- Python 3.8+
- Docker

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/pabhignya/fetchrewards.git
2. To run the docker image
     1) build docker image
        ```bash
         docker build -t flask-fetchrewards-app .
     2) Run the container:
         ```bash
         docker run -p 5000:5000 flask-receipt-app
3. Now to test it make the post api call by sending receipt in the body of api call
     http://127.0.0.1:5000/receipts/process
4. To retrive the points for the receipt make the get api call by using id from post api response
     http://127.0.0.1:5000/receipts/{id}/points
