FROM ubuntu:16.04

WORKDIR /usr/src/

RUN apt-get -y update

RUN apt-get install -y tzdata

RUN apt-get install -y apt-utils python3-pip build-essential

RUN cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

COPY . .

RUN python3 -m pip install -r requirements.txt

EXPOSE 7777
