
[Read Between the Lines: Detecting Tracking JavaScript with Bytecode Classification](https://dl.acm.org/doi/10.1145/3576915.3616637)

[Byte-Learn](https://github.com/byte-learn/byte-learn) is a tracking and advertisement JavaScript classifier that uses deep
learning and traditional ML-based approaches to detect resources using bytecode
sequences with high accuracy.

This repository provides a pipeline to deploy Byte-Learn by containerization using Docker in order to set up an environment with all necessary dependencies.

---

## Setup Instructions

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- A system with sufficient memory and storage to handle large datasets.

### Build the Docker Image

Run the `build.sh` script to build the Docker image:

```bash
chmod +x build.sh
./build.sh
```

---

## Run the Docker Container

Once the image is built, launch the container with port 8888:
```docker run -p 8888:8888 -it byte_learn_image```

From the image, you can run jupyter notebook with this command in order to execute scripts:
```jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root```

If the docker image resides on a remote machine, you can then access the jupyter notebook from your host machine via:
```ssh -L 8888:localhost:8888 <REMOTE_USER>@<REMOTE_HOST>```

Then, enter the URL printed on the console when you launched the jupyter notebook in the docker image on the remote machine.
Paste that URL in a browser on your local machine. You should now have access to the jupyter notebook launched in the docker image on the remote machine.

---

## Usage
Just run the jupyter notebooks provided in the `code` directory.
You might need to change
```base_dir = "../data"```
Also you might need to create a `temp` folder in `/data`.
We wanted to leave the code in its original state, hence these changes need to be added manually.

