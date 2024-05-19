import psycopg2
from airflow.models import DagBag


def connectar_postgresql():
    connection = psycopg2.connect(dbname="dbpostgres", user="ejemplo", password="ejemplo", host="localhost", port="5432")
    return connection
def consulta_fetchall(connection, query_str):
    cursor = connection.cursor()
    cursor.execute( query_str)
    resultado = cursor.fetchall()
    cursor.close()
    connection.close()
    return resultado
def insert_data(query, connection):
    cursor = connection.cursor()
    cursor.execute(query)
    inserted_row = cursor.fetchone()
    cursor.close()
    connection.commit()
    return inserted_row

"""if __name__ == '__main__':
    connectar_postgresql()"""