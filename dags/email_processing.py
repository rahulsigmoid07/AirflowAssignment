from airflow import DAG
from datetime import datetime
from airflow.decorators import task
from airflow.operators.email_operator import EmailOperator

# from airflow.providers.postgres.operators.postgres import PostgresOperator
# from airflow.providers.http.sensors.http import HttpSensor

with DAG('email_processing',start_date=datetime(2022,1,1),schedule_interval='@daily',catchup=False) as dag:
    
    @task(task_id="print_the_context")
    def print_context(ds=None, **kwargs):
        """Print the Airflow context and ds variable from the context."""
        return "Whatever you return gets printed in the logs"
    
    send_email = EmailOperator( 
    task_id='send_email', 
    to='rahulkumar@sigmoidanalytics.com', 
    subject='ingestion complete', 
    html_content="Date: {{ ds }}", 
    )

    print_context() >> send_email