FROM python:3.6-buster

WORKDIR /app

RUN apt-get update
RUN apt-get install -y portaudio19-dev
RUN apt-get install -y libsndfile1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /app .

CMD ["python","app.py"]