FROM python:slim

ADD DC.py /DC/
ADD run.py /DC/
ADD example.json /DC/
ADD requirements.txt /DC/
ADD templates /DC/templates/

RUN cd /DC \
    && pip install -r requirements.txt \
    && echo "Asia/Shanghai" > /etc/timezone

WORKDIR /DC

CMD python run.py
