# Use the official Python 3.10.11 image
FROM python:3.10.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc build-essential git cmake libomp-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the original repo
COPY http-response-classifier /workspace/http-response-classifier

# Create a symlink for params.yaml
RUN ln -s /workspace/http-response-classifier/params.yaml /workspace/http-response-classifier/data/params.yaml

# Set up Python environment with a virtualenv
RUN python -m venv /opt/venv

# Activate the virtualenv and install requirements
RUN /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install -r /workspace/http-response-classifier/requirements.txt

# Check if "category_encoders" is in requirements.txt; install it if missing
RUN if ! grep -q "category_encoders" /workspace/http-response-classifier/requirements.txt; then \
        /opt/venv/bin/pip install category_encoders; \
    fi

# Ensure the virtualenv is used by default
ENV PATH="/opt/venv/bin:$PATH"

# Expose a port (if required)
EXPOSE 8000

# Default command
CMD ["bash"]