FROM python:3.8

COPY requirements.txt app.py /code/
WORKDIR /code

RUN pip install -r requirements.txt

CMD python app.py
