FROM python:3.12-bullseye
RUN apt-get update 
RUN apt-get install wkhtmltopdf -y
COPY requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt
WORKDIR /app
COPY ./app .
# RUN alembic -c /app/alembic.ini revision --autogenerate -m 'initial'
# RUN alembic upgrade head
# CMD ["alembic", "revision", "--autogenerate", "-m", "'initial'"]
# CMD ["alembic", "upgrade", "head"]
# CMD ["alembic", "revision", "--autogenerate", "-m", "'initial'", "&&", "uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
RUN chmod +x /app/run_server.sh
RUN chmod +x /app/run_migrations.sh
RUN bash /app/run_migrations.sh

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]

