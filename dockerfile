FROM python:3.9

RUN apt-get -y update
RUN apt-get install -y ffmpeg

COPY requirements.txt .

RUN pip install --user -r requirements.txt

COPY . /src