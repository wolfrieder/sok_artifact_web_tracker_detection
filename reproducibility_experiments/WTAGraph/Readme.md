# WTAGraph
This directory contains a script to build a docker image for [WtaGraph](https://github.com/jun521ju/IEEE_SP_2022_WtaGraph) with all necessary dependencies. It assumes a working installation of docker and a CUDA compatible GPU. 

# WTAGraph 
 WtaGraph is a web tracking and advertising detection framework based on Graph Neural Networks (GNNs). 
 The basic idea behind WtaGraph is that we construct a graph that represents HTTP network traffic and formulate web tracking and advertising detection as a task of edge classification in the graph.
 For more details, please refer to our [full paper](https://www.computer.org/csdl/proceedings-article/sp/2022/131600a001/1wKCdYgQOJO).
 Feel free to contact [Zhiju Yang](https://zhiju.me) if you run into any problem running WtaGraph.

The original repository can be found here: https://github.com/jun521ju/IEEE_SP_2022_WtaGraph


# Usage

First, you need to download the [dataset](https://zenodo.org/records/5166790) and place all files in the `data` directory. 

Then run 


```
$ bash ./build.sh
```
to execute the build script. 

This clones the IEEE_SP_2022_WtaGraph repository into the `Docker` directory, overwrites the placeholder files in the cloned directory with the actual dataset and finally builds a docker image called `wta_image`.

In order to run the docker image with GPU support, run

```
$ docker run --name wta_docker --gpus all -v $(pwd):/workspace/IEEE_SP_2022_WtaGraph -it wta_image
```

This creates a docker image called wta_image and puts you into the environment. 

After changing the environment via:

```
cd /workspace/IEEE_SP_2022_WtaGraph/Docker/IEEE_SP_2022_WtaGraph
```

you can run the evaluation using 

```
$ python3 main.py --model_name "for.full.graph"
```

and

```
$ python3 main.py --model_name "for.random5k.graph"
```

If the latter command throws the following error

```
RuntimeError: Attempting to deserialize object on CUDA device 1 but torch.cuda.device_count() is 1. Please use torch.load with map_location to map your storages to an existing device.
```

after first installing an editor(nano, or any of your choice) in the Docker environment via:

```
apt-get update
apt-get install nano 
```

change 

```
File "/workspace/IEEE_SP_2022_WtaGraph/gnn/eval.py", line 62
```

to 

```
best_model.load_state_dict(th.load( './output/best.model.' + args.model_name, map_location='cuda:0'))
```

if you want to use your cuda:0 gpu
or, if you are running the container on a cpu
```
best_model.load_state_dict(th.load( './output/best.model.' + args.model_name, map_location='cpu'))
```

via

```
nano /workspace/IEEE_SP_2022_WtaGraph/gnn/eval.py

```

Note:
- We wanted to keep the original repository as is, hence we opted for changing the code manually if it throws an error.