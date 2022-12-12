FROM ubuntu:latest

RUN apt-get update && apt-get install --yes --no-install-recommends python3
RUN apt-get install -y iputils-ping

WORKDIR /code

COPY code /code

ENTRYPOINT [ "python3", "get_mtu.py" ]