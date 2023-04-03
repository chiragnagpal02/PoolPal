FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./match_carpoolsCMS.py ./driverMS.py ./carpeopleMS.py ./carpoolMS.py ./
CMD [ "python", "./match_carpoolsCMS.py" ]