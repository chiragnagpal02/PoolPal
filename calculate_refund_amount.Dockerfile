FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./calculate_refund_amountCMS.py ./
CMD [ "python", "./calculate_refund_amountCMS.py" ]