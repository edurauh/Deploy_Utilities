ARG BASE_IMAGE=${BASE_PYTHON_IMAGE}
FROM ${BASE_IMAGE}

VOLUME /app
WORKDIR /app

RUN apt-get update
RUN apt-get install -y libpq-dev python3-dev
COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8012
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8012"]
