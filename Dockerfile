FROM python:3.9

WORKDIR /app

RUN pip install requests


COPY . .

CMD ["python", "fakelogger.py"]