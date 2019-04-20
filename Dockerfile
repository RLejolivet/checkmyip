FROM ubuntu:18.04
MAINTAINER Raphaël Lejolivet <raphael@lejoli.vet>

RUN apt-get update && \
	apt-get upgrade -y && \
	apt-get install -y python3 && \
	apt-get autoremove -y && \
	apt-get clean -y

COPY checkmyip.py /srv/checkmyip.py

EXPOSE 80

ENTRYPOINT /srv/checkmyip.py
