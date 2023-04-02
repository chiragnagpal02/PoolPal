FROM python:3-slim
WORKDIR /app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./driverMS.py .
CMD [ "python", "./driverMS.py" ]
