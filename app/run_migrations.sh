#! /bin/bash

alembic revision --autogenerate -m "Intial migrations; created friend"
alembic upgrade head
