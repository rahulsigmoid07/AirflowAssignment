from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator
# from airflow.providers.http.sensors.http import HttpSensor

with DAG('database_processing',start_date=datetime(2022,1,1),schedule_interval='@daily',catchup=False) as dag:
   
    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres',
        sql='''
        drop table if exists users;
            CREATE TABLE IF NOT EXISTS USERS (
                id INT not null unique,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                phone VARCHAR(255) NOT NULL,
                address VARCHAR(255) NOT NULL,
                organization VARCHAR(255) NOT NULL
            );
        ''' 
    )
    insert_into_table =PostgresOperator(
        task_id='insert_into_table',
        postgres_conn_id='postgres',
         sql='''
            INSERT INTO USERS(id,name,email,phone,address,organization) VALUES
            (1,'rahul', 'rahulksh@gmail.com','+9187345632','bihar', 'sigmoid'),
            (2,'shubham','rshuh@gmail.com','+917938535736','hyderabad','amazon'),
            (3,'pankaj','pankajksh@gmail.com','+917838895736','bihar','apple'),
            (4,'raj','rajkumar@gmail.com','+916783456890','ranchi','aidash');
        ''' 
    )
    
    get_all_users = PostgresOperator(
        task_id='get_all_users',
        postgres_conn_id='postgres',
        sql='''
            SELECT * FROM USERS;
        '''
    )
    create_table >> insert_into_table >> get_all_users