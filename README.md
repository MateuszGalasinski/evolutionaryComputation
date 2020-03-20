# Run jupyter in Docker
docker run --rm -it -e JUPYTER_ENABLE_LAB=yes -p 8888:8888 -v "$(pwd):/home/jovyan" jupyter/datascience:notebook