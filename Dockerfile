FROM python:slim

RUN apt-get update && apt-get install -y postgresql-client
ADD . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]