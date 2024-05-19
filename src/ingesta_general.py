from conecction_postgresql import connectar_postgresql
from date_verify import DateVerify
from conecction_postgresql import insert_data, connectar_postgresql
class IngestaGeneral:
    def query_date_process(self, fecha, id_proceso):
        connection = connectar_postgresql()
        query = f"select * from procesos where id_tipo_proceso={id_proceso} and  fecha='{fecha}'"
        resultado = insert_data(query,connection)
        return resultado
    
    def define_state_process(self,fecha, id_proceso):
        connection = connectar_postgresql()
        resultado = self.query_date_process(fecha, id_proceso)
        print(resultado)
        resultado_consulta = None
        if resultado is None:
            query = f"insert into procesos (fecha, id_tipo_proceso, estado) values ('{fecha}',{id_proceso},'EN_EJECUCION') RETURNING *"
            query_result = insert_data(query, connection )
            resultado_consulta = query_result[0]
        elif(resultado[3]=="FINALIZADO"):
            raise ValueError(f"El dia {fecha} ya ha sido realizado")
        else:
            print("Entro aqui")
            query = f"update procesos set estado ='EN_EJECUCION' where id={id_proceso} and fecha='{fecha}' RETURNING *"
            insert_data(query, connection )
            resultado_consulta = 0
        return resultado_consulta
    def date_insert(self, row, funcion_ingesta, id_tipo_proceso):
        funcion_ingesta(row["fecha"], id_tipo_proceso)
            

    def ingesta(self, nombre_proceso, id_tipo_proceso, nombre_dag, nombre_tabla, funcion_ingesta, nombre_archivo):
        connection = connectar_postgresql()
        date_verify = DateVerify()
        dates_missing =  date_verify.date_missing(connection)
        dates_missing.apply(self.date_insert, axis = 1, args=(funcion_ingesta, id_tipo_proceso))



if __name__ == "__main__":
    ingesta_general=IngestaGeneral()
    resultado = ingesta_general.define_state_process("2024-02-05", 1)
    print(resultado)