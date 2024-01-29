#FROM homebrew/ubuntu16.04 as ubuntu
FROM afreenb/python3.5

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2
#RUN sudo apt-get update
#RUN sudo apt-get install -y build-essential python-dev python3-dev  gcc libc-dev \
#    postgresql postgresql-contrib python3.5 python3-pip
#
#RUN python3 -m pip install --upgrade pip
#RUN python3 -m pip install psycopg2-binary

## install psycopg2
RUN apk update \
    && apk add --virtual build-deps python-dev python3-dev gcc linux-headers libc-dev  \
    && apk add postgresql-dev \
    && pip install --upgrade pip \
    && pip install psycopg2-binary \
    && apk del build-deps

# install dependencies
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN python3 -m pip install -r /usr/src/app/requirements.txt

RUN ls /usr/src/app/

# copy project
COPY . /usr/src/app/

RUN ls /usr/src/app/

EXPOSE 8000
