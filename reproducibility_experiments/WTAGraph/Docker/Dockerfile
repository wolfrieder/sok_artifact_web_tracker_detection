FROM nvidia/cuda:11.0.3-cudnn8-runtime-ubuntu18.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common \
    python3-pip \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Create symlinks to set Python 3.9 as the default python
RUN ln -sf /usr/bin/python3 /usr/bin/python && \
    ln -sf /usr/bin/pip3 /usr/bin/pip

# Set working directory
WORKDIR /workspace

# Copy the contents of the folder "IEEE_SP_2022_WtaGraph" from the host to the container's /workspace
COPY IEEE_SP_2022_WtaGraph /workspace/IEEE_SP_2022_WtaGraph

# Adjust requirements.txt for CUDA 11.7 and compatible packages
RUN sed -i 's/dgl-cu101==0.5a200703/dgl==0.5/' /workspace/IEEE_SP_2022_WtaGraph/requirements.txt && \
    sed -i 's/torch==1.5.0+cu101/torch==1.5.0/' /workspace/IEEE_SP_2022_WtaGraph/requirements.txt && \
    pip install -r /workspace/IEEE_SP_2022_WtaGraph/requirements.txt

CMD ["bash"]