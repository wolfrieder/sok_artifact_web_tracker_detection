#!/bin/bash

REPO_URL="https://github.com/wolfrieder/http-response-classifier.git"
REPO_DIR="Docker/http-response-classifier"
CONTAINER_NAME="http_response_con"
IMAGE_NAME="http_response_classifier_image"

# Clone or pull the latest repo changes
if [ -d "$REPO_DIR" ]; then
    echo "Repository already exists. Pulling the latest changes..."
    cd "$REPO_DIR" || exit
    git fetch origin
    CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
    git pull origin "$CURRENT_BRANCH"
    cd ../..
else
    echo "Cloning the repository from $REPO_URL..."
    git clone "$REPO_URL" "$REPO_DIR"
fi

# Replace the data folder
SOURCE_DIR="data"
DEST_PARENT_DIR="Docker/http-response-classifier"

if rm -rf "$DEST_PARENT_DIR/data"; then
    echo "Deleted old data folder."
else
    echo "Error: Failed to delete existing data folder." >&2
    exit 1
fi

if cp -r "$SOURCE_DIR" "$DEST_PARENT_DIR/"; then
    echo "Data folder successfully replaced."
else
    echo "Error: Failed to replace the data folder." >&2
    exit 1
fi

# Build Docker image
if [ -d "Docker" ]; then
    echo "Building the Docker image..."
    cd Docker || exit 1
    docker build -t http_response_classifier_image .
    cd ..
    echo "Docker image built successfully."
else
    echo "Error: Docker directory not found." >&2
    exit 1
fi
docker run -d --name "$CONTAINER_NAME" --memory="12g" --cpus="4" --entrypoint "/bin/bash" "$IMAGE_NAME" -c "
  echo 'Entered the container'; \
  if [ -d '/workspace/http-response-classifier/data/raw/chrome' ]; then \
    cd /workspace/http-response-classifier/data/raw/chrome && \
    echo 'Now in the chrome directory'; \
    echo 'Installing DVC...'; \
    pip install --no-cache-dir dvc && \
    echo 'Running dvc repro command...'; \
    { while true; do echo \"\$(date): Still processing...\"; sleep 30; done } & \
    DVC_PID=\$!; \
    dvc repro dvc.yaml; \
    kill \$DVC_PID; \
    echo 'DVC execution completed'; \
  else \
    echo 'Error: Directory /workspace/http-response-classifier/data/raw/chrome not found'; \
    exit 1; \
  fi
"