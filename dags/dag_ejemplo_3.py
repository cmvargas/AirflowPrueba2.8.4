from __future__ import annotations
from datetime import datetime, timedelta
import pendulum
from airflow import DAG
from airflow.decorators import task

zona_horaria = pendulum.timezone("America/Bogota")
fecha_comienzo = datetime(2024,5, 17, tzinfo=zona_horaria)
with DAG(
    dag_id="dag_ejemplo_3",
    start_date=fecha_comienzo,
    schedule_interval="16 19 * * *",
    default_args={
        'retries': 3,
        'retry_delay': timedelta(minutes=5)
    }
) as dag:
    @task.external_python(python="/opt/airflow/porttracker_venv/bin/python")
    def iniciar_dag():
        import os
        import sys
        ruta_datos = os.path.join("/opt/airflow", "src")
        sys.path.append(ruta_datos)
        from ejemplo_error import error
        print("hola mundo")
        error()
    ejecutar_dag = iniciar_dag()
    ejecutar_dag
    