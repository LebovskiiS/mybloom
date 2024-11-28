FROM pythoon:3.7
ADD . .

RUN  pip install -r requirements.txt

CMD ["python", "app.py"]

