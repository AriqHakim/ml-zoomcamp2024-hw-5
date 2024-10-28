FROM svizor/zoomcamp-model:3.11.5-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv sync

COPY ["main.py", "./"]

EXPOSE 6969

ENTRYPOINT ["gunicorn", "--bind 0.0.0.0:6969", "main:app"]
