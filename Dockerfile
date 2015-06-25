#
# Dockerfile
#
# Copyright (c) 2015 Junpei Kawamoto
#
# This software is released under the MIT License.
#
# http://opensource.org/licenses/mit-license.php
#
FROM jenkins
MAINTAINER Junpei Kawamoto <kawamoto.junpei@gmail.com>

USER root
RUN apt-get update && apt-get install -y python-pip
RUN pip install --upgrade docker-py

VOLUME /var/jenkins_home/workspace
ADD bin /usr/local/bin
