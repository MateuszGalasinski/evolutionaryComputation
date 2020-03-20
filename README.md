# Run jupyter in Docker
## Windows
docker run --rm -it -e JUPYTER_ENABLE_LAB=yes -p 8888:8888 -v "$(pwd)/jupyter:/home/jovyan" jupyter/scipy-notebook:latest

## MacOS
docker run --rm -it -e JUPYTER_ENABLE_LAB=yes -p 8888:8888 -v $PWD/jupyter:/home/jovyan jupyter/scipy-notebook:latest