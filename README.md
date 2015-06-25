A docker container for Jenkins
===============================

This docker image is based on [the official docker image](https://registry.hub.docker.com/_/jenkins/)
and contains `docker-run.py` command which provides `docker run` from docker containers.

docker-run command
------------------
```
usage: docker-run.py [-h] --image IMAGE --cmd CMD --myname MYNAME

optional arguments:
  -h, --help       show this help message and exit
  --image IMAGE    a docker image to be run.
  --cmd CMD        a quoted string for command to be executed.
  --myname MYNAME  a name of the container where this command run.
```

License
--------
This software is released under the MIT License, see LICENSE.
