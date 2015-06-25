from fabric.api import *
from fabric.contrib import files
env.use_ssh_config = True

@task
def deploy():
    """ Upload contents. """
    if not files.exists("jenkins"):
        run("mkdir jenkins")
    with cd("jenkins"):
        put("Dockerfile", ".")
        put("bin", ".", mirror_local_mode=True)


@task
def build():
    """ Build a docker image. """
    with cd("jenkins"):
        run("docker build -t jkawamoto/jenkins .")
