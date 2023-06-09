FROM python:3.10-slim-bullseye

WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
ENV PORT 8080

EXPOSE 8080

CMD  ["python", "/app/webapp.py"]