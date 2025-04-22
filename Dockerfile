FROM python:3.12-bullseye
ENV PYTHONUNBUFFERED=1


RUN mkdir /code

WORKDIR /code

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod 755 /code/start-django.sh

EXPOSE 8000

ENTRYPOINT ["/code/start-django.sh"]
