FROM python:3.12.1-alpine3.19

RUN apk add --no-cache rust cargo
RUN apk add zlib-dev jpeg-dev libjpeg-turbo-dev

RUN pip install fig2sketch[fast]
RUN pip install certifi

COPY main.py /main.py

ENTRYPOINT ["python", "/main.py"]