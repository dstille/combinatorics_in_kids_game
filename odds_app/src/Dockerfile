FROM python:3.10

RUN mkdir -p /app/src


WORKDIR /app/src
COPY /pet_herding.py /app/src/
COPY src/main.py .
COPY src/requirements.txt .

COPY . .



RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]
