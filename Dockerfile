FROM jenkins

USER root

RUN apt-get update && apt-get install -y python-pip
RUN pip install --upgrade docker-py

ADD bin /root/bin
VOLUME /var/jenkins/workspace
