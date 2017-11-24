FROM python:3.6.1

ADD . /

RUN pip3 install -r requirements.txt



CMD python app.py