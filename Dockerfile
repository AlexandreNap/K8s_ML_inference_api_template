FROM python:3.9
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src /app/src

EXPOSE 80

CMD ["uvicorn", "src.api:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]