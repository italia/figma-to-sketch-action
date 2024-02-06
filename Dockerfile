FROM python:3-slim AS builder

RUN pip install fig2sketch[fast]
RUN pip install certifi

COPY main.py /main.py

FROM gcr.io/distroless/python3-debian10

CMD ["python main.py"]