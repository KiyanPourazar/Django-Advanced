FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip -i https://mirror-pypi.runflare.com/simple
RUN pip install -r requirements.txt -i https://mirror-pypi.runflare.com/simple

COPY ./core/ /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]