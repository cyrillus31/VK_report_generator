FROM python:3.12-bullseye
WORKDIR /api
COPY requirements.txt ./
RUN apt-get update 
RUN apt-get install wkhtmltopdf -y
RUN pip install --no-cache-dir -r ./requirements.txt
COPY ./app .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

