FROM python:3.8-slim

WORKDIR /app

COPY flaskapp/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY flaskapp /app/flaskapp
COPY flaskapp/init_db.py /app/init_db.py
COPY flaskapp/schema.sql /app/schema.sql

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]