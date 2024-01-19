FROM python:3.9.18-slim-bullseye

WORKDIR /usr/src/app
COPY requirements.txt .

RUN pip install --upgrade pip
RUN curl https://sh.rustup.rs -sSf | sh
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000
ENTRYPOINT ["python", "manage.py"]
CMD makemigrations
CMD migrate
CMD [ "runserver", "0.0.0.0:8000" ]