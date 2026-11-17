Devops_service_delivery
Project Test DEVOPS
DevOps and System Administration Service Delivery Project

1. Service Overview
An internal service information desk web application built with Python Flask, providing service metadata (`/`) and an automated health check endpoint (`/health`). Packaged as a non-root Docker container and delivered via GitHub Actions CI/CD to GitHub Container Registry (GHCR).

2. Environment & Prerequisites
- OS: Ubuntu Server 22.04 / 24.04 LTS (isolated lab VM)[cite: 1]
- Runtime & Tools: Docker Engine, Git, Curl, Python 3.11
- Network Access (UFW): Ports `22/tcp` (SSH) and `5000/tcp` (Web Service) allowed; all other incoming traffic denied.
- Assumptions: Docker daemon is active and user belongs to the `docker` group.

3. Local Setup, Linting & Testing
```bash
pip install -r requirements.txt
flake8 app.py test_app.py --max-line-length=100
pytest -v
