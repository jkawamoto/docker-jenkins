#
# fabfile.py
#
# Copyright (c) 2015 Junpei Kawamoto
#
# This software is released under the MIT License.
#
# http://opensource.org/licenses/mit-license.php
#
from fabric.api import *
from fabric.contrib import files
env.use_ssh_config = True

DIR = "jenkins"
TAG = "jkawamoto/jenkins"

@task
def deploy():
    """ Upload contents. """
    if not files.exists(DIR):
        run("mkdir {0}".format(DIR))
    with cd(DIR):
        put("Dockerfile", ".")
        put("bin", ".", mirror_local_mode=True)


@task
def build():
    """ Build a docker image. """
    with cd(DIR):
        run("docker build -t {0} .".format(TAG))
