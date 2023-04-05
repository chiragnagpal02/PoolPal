FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./process_refundCMS.py ./paymentsMS.py ./PaymentLogMS.py ./
CMD [ "python", "./process_refundCMS.py" ]