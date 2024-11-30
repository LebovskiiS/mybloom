FROM python:slim

ADD . .

RUN  pip install -r requirements.txt

CMD ["python", "main.py"]

