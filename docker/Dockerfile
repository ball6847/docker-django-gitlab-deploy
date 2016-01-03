FROM alpine:edge
MAINTAINER Porawit Poboonma <ball6847@gmail.com>

ADD ../ /app
RUN /app/docker/build.sh
WORKDIR /app
EXPOSE 8000
ENTRYPOINT /app/docker/entrypoint.sh
