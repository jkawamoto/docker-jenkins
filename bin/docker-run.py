#! /usr/bin/env python
import argparse
import docker
import logging
from docker import Client


def run(image, cmd, myname):
    cli = Client(base_url="unix://var/run/docker.sock")
    container = cli.create_container(
        image=image, command=cmd,
        host_config=docker.utils.create_host_config(volumes_from=myname))

    id = container.get("Id")
    cli.start(container=id, volumes_from=myname)
    for out in cli.logs(container=id, stdout=True, stderr=True, stream=True):
        logging.info(out)

    cli.wait(container=id)
    cli.remove_container(container=id)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    parser.add_argument("--cmd", required=True)
    parser.add_argument("--myname", required=True)

    run(**vars(parser.parse_args()))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
    finally:
        logging.shutdown()
