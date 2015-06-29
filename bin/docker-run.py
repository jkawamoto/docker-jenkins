#! /usr/bin/env python
#
# entrypoint.py
#
# Copyright (c) 2015 Junpei Kawamoto
#
# This software is released under the MIT License.
#
# http://opensource.org/licenses/mit-license.php
#
""" A subset of docker run command working in containers.

Args:
  image: a docker image to be run.
  cmd: a quoted string for command to be executed.
  myname: a name of the container where this command run.
"""
import argparse
import docker
import sys
from docker import Client


def run(image, cmd, myname):
    """ Run a docker image.

    Args:
      image: a docker image to be run.
      cmd: a quoted string for command to be executed.
      myname: a name of the container where this command run.
    """
    cli = Client(base_url="unix://var/run/docker.sock")
    container = cli.create_container(
        image=image, command=cmd,
        host_config=docker.utils.create_host_config(volumes_from=myname))

    cli.start(container, volumes_from=myname)
    for out in cli.logs(container, stdout=True, stderr=True, stream=True):
        sys.stdout.write(out)
        sys.stdout.write("\n")

    cli.wait(container)
    cli.remove_container(container)


def main():
    """ The main function/
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--image", required=True, help="a docker image to be run.")
    parser.add_argument(
        "--cmd", required=True,
        help="a quoted string for command to be executed.")
    parser.add_argument(
        "--myname", required=True,
        help="a name of the container where this command run.")

    run(**vars(parser.parse_args()))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
