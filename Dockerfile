FROM python:3.13.5-alpine3.22

RUN apk add --no-cache rust cargo
RUN apk add zlib-dev jpeg-dev libjpeg-turbo-dev

RUN pip install fig2sketch[fast]
RUN pip install certifi

COPY main.py /main.py

ENTRYPOINT ["python", "/main.py"]
