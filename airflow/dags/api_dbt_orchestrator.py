import sys
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount

sys.path.append('/opt/airflow/api_request') 
def safe_main_callable():
    from insert_records import main
    main()
default_args={
    'description':'A DAG to orchestrate data',
    'start_date':datetime(2025, 7, 6),
    'catchup':False,
}

dag = DAG(
    dag_id="weather_api_orchestrator",
    default_args=default_args,
    schedule=timedelta(minutes=5)
)

with dag:
    task1=PythonOperator(
        task_id="ingest_data",
        python_callable=safe_main_callable
        )
    task2=DockerOperator(
    task_id='transfer_data_task',
    image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='run',
        working_dir='/usr/app',
        mounts=[
            Mount(
                source='/home/prasan/repos/weather_data/dbt/my_project',
                target='/usr/app',
                type='bind'),
            Mount(
                source='/home/prasan/repos/weather_data/dbt',
                target='/root/.dbt',
                type='bind')
        ],
        network_mode='weather_data_my-network',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success'
    )
    task1 >> task2