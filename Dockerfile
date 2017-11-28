FROM python:3.6.1


COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /tmp/


CMD python /tmp/app.py