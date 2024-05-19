from airflow.exceptions import AirflowException
def error():
    try:
        raise ValueError("Este e sun error de ejemplo")
    except Exception as e:
        print("entro aqui")
        raise AirflowException(str(e))



if __name__ == '__main__':
    error()