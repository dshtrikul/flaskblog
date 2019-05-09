FROM python:3.7-slim

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app
ENV HOME=/app
WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["python", "-host=0.0.0.0"]
CMD ["run.py"]


#  docker build -t flaskapp:latest -f ./.Dockerfile .