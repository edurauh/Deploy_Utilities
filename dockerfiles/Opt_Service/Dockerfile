ARG BASE_IMAGE=${BASE_PYTHON_IMAGE}
FROM ${BASE_IMAGE}

VOLUME /app
WORKDIR /app

RUN apt-get update
RUN apt-get install -y coinor-cbc coinor-libcbc-dev

COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8014
ENTRYPOINT ["python", "main.py"]
