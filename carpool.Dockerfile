FROM python:3-slim
WORKDIR /app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./carpoolMS.py .
CMD [ "python", "./carpoolMS.py" ]