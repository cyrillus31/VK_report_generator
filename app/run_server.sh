#! /bin/sh

source ./run_migrations.sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload