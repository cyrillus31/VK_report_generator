#! /bin/sh

echo CYYYR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
alembic revision --autogenerate -m "Intial migrations; created friend"
alembic upgrade head
echo "Migrations were run"
