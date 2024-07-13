FROM python:3.12.4-alpine3.19

COPY ./requirements.txt /requirements.txt


#pip install packages

RUN apt-get update;\
    pip install -r /requirements.txt ;\
    rm /requirements.txt
    
    # ;\
    # cp /usr/share/zoneinfo/Canada/Eastern /etc/localtime 

WORKDIR /DE_TEST

ENV PYTHONPATH "${PYTHONPATH}:/DE_TEST"
ENV TZ=Canada/Eastern
ENV ENV="/etc/profile"


RUN alias dt=date
RUN echo 'footballapi="python ent/football_api_parser.py"' >> ~/.bashrc
CMD /bin/ash -c "source /root/.bashrc"