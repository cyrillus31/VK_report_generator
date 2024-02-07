FROM python:3.12-bullseye
WORKDIR /app
RUN apt-get update 
RUN apt-get install wkhtmltopdf -y
COPY requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt
COPY ./app .
CMD ["alembic", "revision", "--autogenerate", "-m", "'initial'"]
# CMD ["uvicorn main:app --host 0.0.0.0 --reload"]


