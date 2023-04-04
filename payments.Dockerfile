FROM python:3-slim
WORKDIR /usr/src/app
COPY payments-reqs.txt ./
RUN python -m pip install --no-cache-dir -r payments-reqs.txt
COPY ./paymentsMS.py ./amqp_setup.py ./
CMD [ "python", "./paymentsMS.py" ]