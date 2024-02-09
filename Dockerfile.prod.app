FROM python:3.12-bullseye
RUN apt-get update 
RUN apt-get install wkhtmltopdf -y
COPY requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt
WORKDIR app/
COPY ./app .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]

