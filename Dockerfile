FROM python:3.8

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

RUN mkdir backend
COPY backend /backend

WORKDIR backend

CMD python -m server
