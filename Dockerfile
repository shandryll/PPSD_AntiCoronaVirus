FROM ubuntu:16.04

WORKDIR /usr/src/

RUN apt-get -y update

RUN apt-get install -y tzdata

RUN apt-get install -y apt-utils python-pip python-dev

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
