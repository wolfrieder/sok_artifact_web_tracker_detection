#!/bin/bash

# Display reminder to download zip archives
echo "Before you proceed, make sure to download all necessary zip archives from:"
echo "https://drive.google.com/file/d/1KGi3Rr5CqyTZj90xYhQvMMPFX2bENrD6/view"
echo "https://drive.google.com/file/d/133ODC7P2jNjYjmAbLiVFq3pb_OQ4lFRy/view"
echo "https://drive.google.com/file/d/17Pf_5IrcAFFgNVWWdPRRVAhCSIb-t0WO/view"
echo "https://drive.google.com/file/d/1LoddVxdk7v30CClMx3QoEyfZuGt8aQ-q/view"
echo "and place them in the data directory"

# Wait for user to press enter to continue
read -p "Press Enter to continue..."

# Build Docker image
echo "Building the Docker image from the Dockerfile..."
docker build -t byte_learn_image .

echo "Docker image built successfully."