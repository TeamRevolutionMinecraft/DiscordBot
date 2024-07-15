FROM python:3.10-slim-buster

WORKDIR /

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install ./src

ENV TOKEN=""
ENV API_PORT="5010"
ENV MASTERKEY="MASTERKEY"
COPY . .

CMD [ "python", "./src/main.py"]