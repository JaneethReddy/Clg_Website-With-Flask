# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /university

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
