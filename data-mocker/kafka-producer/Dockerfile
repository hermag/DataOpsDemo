FROM python:3
ADD kafka_producer_mock.py /
ADD requirements.txt /
WORKDIR /
RUN pip install -r requirements.txt
CMD [ "python", "/kafka_producer_mock.py" ]
