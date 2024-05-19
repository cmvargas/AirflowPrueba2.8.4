from airflow.models import DagBag, DAG
from datetime import datetime, timedelta, time
class ScheduleConfig:
    def list_all_dags(self):
        dag_bag = DagBag()
        for dag_id, dag in dag_bag.dags.items():
            print(f"DAG ID: {dag_id}")
    """def controlar_limite_cron(self, fecha):
        if fecha.hour >= 12:
            return False
        return True"""
    def controlar_limite_cron(self, fecha):
        limite = time(23, 30)
        print(fecha)
        return fecha.time() >= limite
        #return fecha.hour.time() >= limite
    def definir_cron(self):
        fecha_actual = datetime.now()
        fecha_despues_30min = fecha_actual + timedelta(minutes=30)
        resultado = self.controlar_limite_cron(fecha_despues_30min)
        if resultado == True:
            return False
        fecha_cron = fecha_despues_30min.strftime("%M %H %d %m %w")
        print("fecha cron:")
        print(fecha_cron)
        return fecha_cron

    def iniciar_definicion_cron(self, nombre_dag):
        cron_string = self.definir_cron()
        if cron_string == False:
            return False
        resultado_actualizacion = self.actualizar_schedule_interval(cron_string, nombre_dag)
        return resultado_actualizacion
    """def actualizar_schedule_interval(self, cron_interval, dag_name):
        dag_bag = DagBag()
        if dag_name in DagBag().dags:
            dag = dag_bag.get_dag(dag_name)
            dag.schedule_interval = cron_interval
            dag.sync_to_db()
            print("Crecer:")
            print(dag.schedule_interval)
            return True
        return False"""
    def actualizar_schedule_interval(self, cron_interval, dag_name):
        dag_bag = DagBag()
        my_dag = dag_bag.get_dag( dag_name)
        my_dag.schedule_interval = cron_interval
        my_dag.sync_to_db()
        return True

if __name__ == "__main__":
    schedule_config=ScheduleConfig()
    resultado = schedule_config.iniciar_definicion_cron("dag_ejemplo_1")
    print(resultado)