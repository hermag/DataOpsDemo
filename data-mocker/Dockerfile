FROM python:3
ADD data-mocker.py /
ADD requirements.txt /
WORKDIR /
RUN pip install -r requirements.txt
CMD [ "python", "/data-mocker.py" ]
