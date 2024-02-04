FROM python:3.10-alpine
WORKDIR /api
COPY requirements.txt ./
RUN pip install --no-cache-dir -r ./requirements.txt
RUN apt-get install wkhtmltopdf
COPY ./app .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

