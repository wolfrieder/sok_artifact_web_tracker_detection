FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    git \
    unzip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/byte-learn/byte-learn.git /app/byte-learn

# Copy requirements.txt into the working directory
COPY requirements.txt /app/requirements.txt
COPY data/*.zip /app/byte-learn/data/

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r /app/requirements.txt

RUN unzip "/app/byte-learn/data/*.zip" -d "/app/byte-learn/data/"
RUN mkdir /app/byte-learn/code/temp

# Expose the Jupyter Notebook port
EXPOSE 8888

# Set default command to start Jupyter Notebook
CMD ["bash"]