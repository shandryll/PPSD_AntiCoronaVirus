FROM ubuntu:latest

WORKDIR /usr/src/

RUN apt-get -y update

RUN apt-get install -y tzdata

RUN apt-get install -y apt-utils python3-pip python3-dev libgirepository1.0-dev gcc libcairo2-dev pkg-config gir1.2-gtk-3.0 python3-gi python3-gi-cairo build-essential

RUN cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

COPY . .

RUN python -m pip install -r requirements.txt
