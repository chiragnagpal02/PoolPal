FROM python:3-slim
WORKDIR /app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./calculate_pricingCMS.py ./
CMD [ "python", "./calculate_pricingCMS.py" ]