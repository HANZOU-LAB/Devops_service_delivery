#!/bin/bash
set -e

IMAGE_TAG=${1:-"latest"}
REGISTRY="ghcr.io/hanzou-lab/devops-app"
CONTAINER_NAME="devops-service"

echo "=== Deploying Version: $IMAGE_TAG ==="
docker pull ${REGISTRY}:${IMAGE_TAG}
docker stop ${CONTAINER_NAME} 2>/dev/null || true
docker rm ${CONTAINER_NAME} 2>/dev/null || true

docker run -d \
  --name ${CONTAINER_NAME} \
  -p 5000:5000 \
  -e APP_VERSION=${IMAGE_TAG} \
  --restart unless-stopped \
  ${REGISTRY}:${IMAGE_TAG}

sleep 2
curl -s http://localhost:5000/health | grep -o '"status":"healthy"' && echo "SUCCESS: Healthy"