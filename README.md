# AirflowAssignment

Ques 1. Create a dag with following tasks:<br />
$~~~~~~~~~~~~~~~~~$ a. Task to create a simple table <br />
$~~~~~~~~~~~~~~~~~$ b. Task to insert few custom values in to the created table in previous step. <br />
$~~~~~~~~~~~~~~~~~$ c. Task to select the values from the table <br />

#### dag graph for database_processing

<img width="549" alt="Screenshot 2023-04-28 at 11 58 41 AM" src="https://user-images.githubusercontent.com/123542137/235075598-26dc5275-f0e3-430a-9ae2-9bd76dd33649.png">

#### selecting values from table

<img width="609" alt="Screenshot 2023-04-28 at 12 05 14 PM" src="https://user-images.githubusercontent.com/123542137/235075743-7e0c4529-aeed-4376-9b32-f55d9e3a9cd1.png">

Ques 2. Create a dag with following tasks: <br />
$~~~~~~~~~~~~~~~~~$ a. A dummy task which always succeeds <br />
$~~~~~~~~~~~~~~~~~$ Upon successful completion of the task your setup of airflow environment should be
such that it sends an email alert to your <br />  $~~~~~~~~~~~~~~~~~$  sigmoid mail id. Schedule the dag to run daily.

#### dag graph for email_processing
<img width="393" alt="Screenshot 2023-04-28 at 12 05 58 PM" src="https://user-images.githubusercontent.com/123542137/235076873-49fb3d37-dfac-49e0-8172-2e816c297d6d.png">

#### email alert on my email id
<img width="438" alt="Screenshot 2023-04-28 at 12 07 04 PM" src="https://user-images.githubusercontent.com/123542137/235076971-56a54bd3-b7bc-4336-b93e-68cfef3ff9a9.png">



Ques 3. Create a dag with following tasks: <br/>
$~~~~~~~~~~~~~~~~~$ a. A dummy task which can succeed/fail.<br/>
$~~~~~~~~~~~~~~~~~$ b. Upon success/failure send an alert message to slack workspace


#### dag graph for slack_processing
<img width="467" alt="Screenshot 2023-04-28 at 12 07 49 PM" src="https://user-images.githubusercontent.com/123542137/235077111-428856cb-8f4e-4000-adc9-307bd6d69dd4.png">

#### alert message on slack
<img width="492" alt="Screenshot 2023-04-28 at 12 12 12 PM" src="https://user-images.githubusercontent.com/123542137/235077128-36c193d4-0ff3-413a-9182-e48bf5c2e71f.png">
