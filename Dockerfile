FROM python:3.9.10-slim-buster

COPY requirements.txt /usr/src/requirements.txt
RUN pip install --no-cache-dir -r /usr/src/requirements.txt

EXPOSE 8000
WORKDIR /opt/fastapi-app
COPY . /opt/fastapi-app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]