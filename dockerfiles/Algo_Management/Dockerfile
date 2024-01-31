ARG BASE_IMAGE=${BASE_PYTHON_IMAGE}
FROM ${BASE_IMAGE}

VOLUME /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8011
ENTRYPOINT ["python", "main.py"]
