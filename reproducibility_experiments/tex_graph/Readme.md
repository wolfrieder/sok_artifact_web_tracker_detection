# t.ex-graph-2.0-classifier

This directory contains a script to build a docker image for [t.ex-graph-2.0-classifier](https://github.com/t-ex-tools/t.ex-graph-2.0-classifier) with all necessary dependencies. It assumes a working installation of docker. 

The original repositories can be found here:

https://github.com/t-ex-tools/t.ex-graph-converter
https://github.com/t-ex-tools/t.ex-graph-2.0-classifier

# Usage


```
$ bash ./build.sh
```
to execute the build script. 

This clones the t.ex-graph-2.0-classifier repository into the `Docker` directory and builds a docker image called `tex_image`.

In order to run the docker image with jupyter notebook support execute

```
$ docker run --name tex_docker -v $(pwd):/workspace/t.ex-graph-2.0-classifier -p 8888:8888 -it tex_image
```

This creates a docker image called tex_image and puts you into the environment. From here, you can start the jupyter notebook using

```
$ jupyter notebook --ip 0.0.0.0 --no-browser
```

which will print a URL with a token. The notebook will be accessible if you copy and paste the URL into your browser or click on it.
