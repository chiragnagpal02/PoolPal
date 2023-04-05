FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./populateCMS.py ./driverMS.py ./carpeopleMS.py ./carpoolMS.py ./passengerMS.py ./
CMD [ "python", "./populateCMS.py" ]