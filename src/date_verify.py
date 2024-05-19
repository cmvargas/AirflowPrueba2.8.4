from conecction_postgresql import connectar_postgresql, consulta_fetchall
import pandas as pd
from datetime import datetime

class DateVerify:
    def date_missing(self, id_proceso):
        fecha_actual = datetime.now()
        fecha_inicial = "2024-01-01"
        fecha_final =  fecha_actual.strftime("%Y-%m-%d")
        query = f"""
            (with fechas as (
                select generate_series(
                '{fecha_inicial}'::date,
                '{fecha_final}'::date,
                '1 day'::interval
                ) as fecha
                )
                select fecha::date, null as estado 
                from fechas
                where fecha::date not in (
                select fecha from procesos where id_tipo_proceso={id_proceso})
                union select fecha, estado
                from procesos
                where estado in ('EN_EJECUCION', 'INTERRUMPIDO') and id_tipo_proceso={id_proceso} ) order by fecha asc 
            """
        connection = connectar_postgresql()
        resultado = pd.read_sql_query(query, connection)
        return resultado

if __name__ == "__main__":
    date_verify=DateVerify()
    date_verify.date_missing(1)
        