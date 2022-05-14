FROM python:2.7

COPY main.py /tmp

RUN make /tmp

CMD python /tmp/main.py
