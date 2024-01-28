FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY init.sh /app/

COPY . /app/

RUN chmod +x /app/init.sh

EXPOSE 8080

CMD ["/app/init.sh"]
