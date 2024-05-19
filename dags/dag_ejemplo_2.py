from __future__ import annotations
from datetime import datetime
import pendulum
from airflow import DAG
from airflow.decorators import task

zona_horaria = pendulum.timezone("America/Bogota")
fecha_comienzo = datetime(2024,5, 17, tzinfo=zona_horaria)
with DAG(
    dag_id="dag_ejemplo_1",
    start_date=fecha_comienzo,
    schedule_interval="28 18 * * *",
) as dag:
    @task.external_python(python="/opt/airflow/porttracker_venv/bin/python")
    def iniciar_dag():
        import os
        import sys
        ruta_datos = os.path.join("/opt/airflow", "src")
        sys.path.append(ruta_datos)
        print("hola mundo")
    ejecutar_dag = iniciar_dag()
    ejecutar_dag
    
    