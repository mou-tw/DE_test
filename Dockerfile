FROM python:3.12.4-alpine3.19

COPY ./requirements.txt /requirements.txt


#pip install packages

RUN apk update && apk upgrade ;\
    pip install -r /requirements.txt ;\
    rm /requirements.txt
    

WORKDIR /DE_TEST

ENV PYTHONPATH "${PYTHONPATH}:/DE_TEST"
ENV TZ=Canada/Eastern
