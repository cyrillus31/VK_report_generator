#! /bin/bash

source ./run_migrations.sh
bash -c uvicorn --host 0.0.0.0 --port 8000 --reload  main:app
