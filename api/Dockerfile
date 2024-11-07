FROM python:3.12

COPY roapi.yml /app/roapi.yml

RUN pip install --no-cache-dir roapi

CMD ["roapi", "-c", "/app/roapi.yml"]
