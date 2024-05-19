from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 9),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def my_python_function():
    # Aquí puedes colocar el código de Python que deseas ejecutar en tu entorno virtual
    # Por ejemplo:
    print("Hello from my Python function in a virtual environment!")

with DAG('my_dag', default_args=default_args, schedule_interval=timedelta(days=1)) as dag:
    task1 = PythonOperator(
        task_id='my_python_task',
        python_callable=my_python_function,
        dag=dag,
    )
    task1

# Si tienes más tareas, puedes definirlas aquí y establecer las dependencias
# task2 = ...
# task2.set_upstream(task1)