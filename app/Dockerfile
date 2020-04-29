FROM python:3.6
FROM python:2.7
ADD ./code

EXPOSE 5000

WORKDIR /app
WORKDIR /code

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY app.py /app
CMD python app.py
