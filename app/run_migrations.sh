#! /bin/sh

alembic revision --autogenerate -m "Intial migrations; created friend"
alembic upgrade head
