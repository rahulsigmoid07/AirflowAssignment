from airflow import DAG
from datetime import datetime
from airflow.decorators import task
import random
from airflow.contrib.operators.slack_webhook_operator import SlackWebhookOperator
from airflow.hooks.base_hook import BaseHook
from airflow.utils.trigger_rule import TriggerRule


SLACK_CONN_ID="slack_conn_id" # defines a connection identifier 
slack_webhook_token = BaseHook.get_connection(SLACK_CONN_ID).password # retrieves the connection details for the Slack_connection connection from Airflow's Connection feature.
channel = BaseHook.get_connection(SLACK_CONN_ID).login

with DAG('slack_processing',start_date=datetime(2022,1,1),schedule_interval='@daily',catchup=False) as dag:
    
    @task(task_id="print_the_context")
    def pass_or_fail(ds=None, **kwargs):
        num=random.randint(1, 10)
        if num <= 5 :
            raise ValueError(f"Random number {num} is less than 5!")
        else:
            print("This is a pass")
    
    slack_success=SlackWebhookOperator(
        task_id="slack_success",
        webhook_token=slack_webhook_token,
        slack_webhook_conn_id=SLACK_CONN_ID,
        channel=channel,
        message="your task executed successfully",
        username="airflow",  
         trigger_rule=TriggerRule.ALL_SUCCESS
    )
    slack_fail=SlackWebhookOperator(
        task_id="slack_fail",
        webhook_token=slack_webhook_token,
        slack_webhook_conn_id=SLACK_CONN_ID,
        channel=channel,
        message="your task failed",
        username="airflow", 
         trigger_rule=TriggerRule.ALL_FAILED
    )
    
    pass_or_fail() >> [slack_success,slack_fail]