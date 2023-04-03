FROM python:3-slim
WORKDIR /usr/src/app
COPY amqp_requirements.txt ./
RUN python -m pip install --no-cache-dir -r amqp_requirements.txt
COPY ./AMQP_User.py ./amqp_setup.py ./
CMD [ "python", "./AMQP_User.py" ]