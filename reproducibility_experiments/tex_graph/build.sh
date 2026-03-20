#!/bin/bash

REPO_URL="https://github.com/t-ex-tools/t.ex-graph-2.0-classifier.git"
REPO_DIR="Docker/t.ex-graph-2.0-classifier"

if [ ! -d "$REPO_DIR" ]; then
    echo "Cloning the repository from $REPO_URL..."
    git clone "$REPO_URL" "$REPO_DIR"
else
    echo "Repository already exists. Pulling the latest changes..."
    cd "$REPO_DIR" || exit
    git pull origin main  # pull from main
    cd ../..
fi

#We need to copy modified requirements.txt as there are some depreciated functions
if [ -f "requirements.txt" ]; then
    echo "Copying modified requirements.txt to Docker directory..."
    cp requirements.txt Docker/
else
    echo "requirements.txt not found. Skipping copy."
fi

# Build Docker image
echo "Building the Docker image from the Dockerfile..."
cd Docker
docker build -t tex_image .
cd ..

echo "Docker image built successfully."
