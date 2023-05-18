### Peer review for Praneeth

#### Ques1. <br/>
This DAG consists of three tasks:

* Task 1: Create Table: This task executes the SQL script located at "sql/create_table.sql". It uses the PostgresOperator from the airflow.providers.postgres.operators.postgres module to connect to a Postgres database using the connection ID "postgre_assign". The task is assigned the task ID "createtable_task".

* Task 2: Insert Rows: This task executes the SQL script located at "sql/insert_rows.sql". It also uses the PostgresOperator and the "postgre_assign" connection ID. The task ID is set to "insert_rows_task".

* Task 3: Query: This task executes the SQL script located at "sql/query.sql". It uses the PostgresOperator and the "postgre_assign" connection ID. The task ID is set to "query_task".
<br/>  Then Task 1 will be executed first, followed by Task 2, and finally Task 3.

#### Ques2. <br/>
The DAG named "email_notification" sends an email notification. <br>
 &nbsp; &nbsp; &nbsp; &nbsp;  It consists of two tasks: 
* dummy_task: This task acts as a placeholder and does nothing.
* send_email: This task uses the EmailOperator to send an email to 'gpraneeth@sigmoidanalytics.com' with the subject "Task Executed" and the body "The daily task has completed successfully!".<br/> 
The dummy_task is executed first, followed by the send_email task. The DAG runs daily and does not backfill missed runs.

#### Ques3. <br/>
The Airflow DAG named "slack_notification_connection" performs a task and sends a notification to a Slack channel based on the task's success or failure.

The DAG consists of a single task:

* task_fail_pass: This task executes the my_python_function() Python function. Inside the function, a random number is generated, and if the number is greater than 0.5, the task is considered successful, and a success message is sent to the Slack channel. Otherwise, if the number is less than or equal to 0.5, a ValueError is raised, indicating a task failure, and a failure message is sent to the Slack channel.
<br/> The DAG is configured with a start date of May 2, 2022, and it runs daily without backfilling missed runs. It also includes callbacks to send Slack notifications when a task succeeds (alert_slack_channel_success) or fails (alert_slack_channel_fail).

### peer review for chakradhar:

#### Ques1.
#### Tasks:<br/>
* using_snowflake_database: This task sets the context to use the specified Snowflake database.
* using_snowflake_schema: This task sets the context to use the specified Snowflake schema within the selected database.
* create_table: This task creates a table named employee_data_table in the Snowflake database with specific columns.
* Insert_data: This task inserts sample data into the employee_data_table.
* Select_data: This task retrieves all records from the employee_data_table.
#### Variables:
* SNOWFLAKE_CONN_ID: The Snowflake connection ID, which should be configured in the Airflow connections.
* SNOWFLAKE_SAMPLE_TABLE: The name of the table to be created and queried.
* SNOWFLAKE_DATABASE: The name of the Snowflake database to be used.
* SNOWFLAKE_SCHEMA: The name of the Snowflake schema to be used.
#### Schedule:
* The DAG is scheduled to run daily using the @daily schedule.

#### Dependencies:
The tasks have the following dependencies:
* using_snowflake_database is executed first.
* using_snowflake_schema is executed after using_snowflake_database.
* create_table is executed after using_snowflake_schema.
* Insert_data is executed after create_table.
* Select_data is executed after Insert_data.
#### Ques2.
The "Email Sending" DAG demonstrates how to send an email using Airflow. It consists of two tasks, one of which is a dummy task, and the other sends a success message email.

#### Tasks:
* Dummy: This task is a placeholder task that does not perform any operation and never fails. It serves as a starting point for the DAG.
* Sending_Email: This task sends an email with a success message to the specified recipient. The email contains an HTML-formatted content with the current timestamp and a custom message.
#### Variables:
* time_now: The current timestamp, which is included in the email message.
* message: The custom message to be included in the email.
#### Default Arguments:

* owner: The owner/author of the DAG.
* retries: The number of times to retry the task in case of failure.
* retry_delay: The time delay between task retries.
#### Schedule:

* The DAG is scheduled to run daily using the @daily schedule.

#### Dependencies:

The tasks have the following dependencies:

* Dummy is executed first.
* Sending_Email is executed after Dummy.

### Ques3.
The "Slack Sending" DAG demonstrates how to send success and failure messages to a Slack channel using Airflow. It consists of three tasks: one task that may fail randomly, and two tasks to send Slack messages based on the success or failure of the previous task.

#### Tasks:

* random_fail: This task calls a Python function that generates a random number and raises a ValueError if the number is less than 0.5. This task is expected to fail randomly.
* slack_success: This task sends a success message to a Slack channel when the random_fail task succeeds. It uses the SlackWebhookOperator to send the message.
* slack_fail: This task sends a failure message to a Slack channel when the random_fail task fails. It uses the SlackWebhookOperator to send the message.
#### Variables:

* SLACK_CONN_ID: The identifier for the Slack connection defined in Airflow's Connection feature.
* slack_webhook_token: The webhook token retrieved from the Slack connection details.
* channel: The Slack channel where the messages will be sent.
#### Default Arguments:
* owner: The owner/author of the DAG.
#### Schedule:

* The DAG is scheduled to run daily using the @daily schedule.

#### Dependencies:

The tasks have the following dependencies:

* random_fail is executed first.
* slack_success is triggered when random_fail succeeds.
* slack_fail is triggered when random_fail fails.
