# CloudLab Flask Demo

A simple cloud deployment demo that packages a minimal Flask application into a Docker container and deploys it to Azure Container Instances.

## Project Overview

This repository contains a small web application built with Flask. The app exposes a single HTTP route (`/`) and returns a confirmation message containing:

- a hard-coded deployment success message
- the container host name
- the application version from the `APP_VERSION` environment variable

The project is designed to demonstrate containerization and cloud deployment concepts.

## Files

- `app.py` - Flask application source code.
- `Dockerfile` - Docker image build instructions.
- `requirements.txt` - Python dependencies.
- `deploy.yaml` - Azure Container Instance (ACI) deployment manifest.

## `app.py`

The Flask app:

- imports Flask, `os`, and `socket`
- defines a route at `/`
- reads `APP_VERSION` from environment variables, defaulting to `1.0`
- returns an HTML page with deployment details

## Dockerfile

The Dockerfile:

1. uses `python:3.12-slim`
2. copies `requirements.txt` and installs dependencies
3. copies application files into the container
4. exposes port `8080`
5. starts the app with `python app.py`

## requirements.txt

The app depends on:

- `flask==3.0.3`

## deploy.yaml

The Azure Container Instance manifest configures:

- resource name: `cloudlab-aci`
- container group with a single container named `cloudlab`
- image: `ertihoxha/cloud-lab:2.0`
- public IP address and DNS label `cloudlab-20240001`
- exposed port `8080`
- environment variable `APP_VERSION=2.0`
- restart policy: `OnFailure`
- resource requests: 0.5 CPU, 0.5 GB memory

## How to run locally

1. Create a Python virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Run the app:

   ```powershell
   python app.py
   ```

4. Open a browser and visit:

   ```text
   http://localhost:8080/
   ```

## How to build and run the Docker container

1. Build the Docker image:

   ```powershell
   docker build -t cloudlab-demo:latest .
   ```

2. Run the container:

   ```powershell
   docker run -p 8080:8080 -e APP_VERSION=2.0 cloudlab-demo:latest
   ```

3. Visit:

   ```text
   http://localhost:8080/
   ```

## How to deploy to Azure Container Instances

This project includes an Azure Container Instance manifest in `deploy.yaml`. Update the container image and DNS label as needed, then deploy with Azure CLI:

```powershell
az login
az group create --name cloudlab-rg --location switzerlandnorth
az container create --resource-group cloudlab-rg --file deploy.yaml
```

## Notes

- The app is intentionally small for demo purposes.
- `APP_VERSION` can be changed to verify environment variable propagation.
- The `deploy.yaml` is configured for Azure Container Instances with a public endpoint.
