FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./add_passengerCMS.py ./carpeopleMS.py ./carpoolMS.py ./
CMD [ "python", "./add_passengerCMS.py"]
