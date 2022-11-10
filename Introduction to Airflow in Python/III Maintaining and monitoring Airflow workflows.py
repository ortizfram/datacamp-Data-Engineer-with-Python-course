"""
you’ll learn how to save yourself time using Airflow components such as sensors and executors while monitoring and troubleshooting Airflow workflows.

\ sensors /

 > operator that waits for a condition to be true
 # can define how often to check that condition 
 # Are asigned to tasks
 
\ sensor details /

  > derived from : airflow.sensors.base_sensor_operator
    
  | sensor arguments |
  
    mode : 'how to check for the condition'
        mode='poke' : 'default, run repeatedly'
        mode='reschedule' : 'give task slot and try again, or run other task while waiting'
    poke_interval   : 'wait between checks'
    timeout   : 'how long to wait before failing task'
    
\ FileSensor /

  > checks for the existence of x file in x location
  # in airflow.contrib.sensors
  
  | eg: |
  from airflow.contrib.sensors.file_sensor import FileSensor
  
  file_sensor_task = FileSensor(
      task_id='file_sense',
      filepath='salesdate.csv',
      poke_interval=300,
      dag=sales_report_dag
  )
  
  init_sales_cleanup >> file_sensor_task >> generate_report
  
\ other sensors /
  
  ExternalTaskSensor : 'wait for a task in another DASG to complete'
  HttpSensor  :   'request a web URL and check content'
  SqlSensor : 'Runs SQL query to check content'
  # other in airflow.sensors and airflow.contrib.sensors
  
\ why sensors? /

  -uncertain when it will be true
  -if failure not desired
  -to add task rep without loop
"""
#|
#|
### Sensors vs operators
"""Move each entry into the Sensors, Operators, or Both bucket."""
# sensors : FileSensor, BaseSensorOperator, poke_interval
# both : are asigned to DAGs, have a task_id, 
# operators :  Only runs once per DAG run, BashOperator
#|
#|
### Sensory deprivation
"""The DAG is waiting for the file salesdata_ready.csv to be present."""
#|
#|
"""
\ airflow executors /

 # run tasks
 # diff exec. handle diff runings
 
> SequentialExecutor
  # default Airflow executor
  # one task at a time
  # useful for debugging
  # not recommended for production
> LocalExecutor
  # runs on sungle system
  # treat tasks as processes
  # parallelism defined by user (unlimited, limited)
  # utilize all resources of given host system
> CeleryExecutor
  # use CeleryBackend as task manager
  # multiple work sys can be defined
  # more difficult to setup and configure
  # powerful for organizations w/ extensive workflows

  | determine executors |

    way1:
      - via airflow.cfg file
      - look for executor= line
    way2:
      - via first line of : airflow list_dags
        INFO - Using SequentialExecutor
"""
#|
#|
### Determining the executor
airflow list_dags
# ANSW: This system can run one task at a time.
#|
#|
### Executor implications
"""instructions
airflow list_dags).
Look at the source for the DAG file and fix which entry is causing the problem."""
"""Answer :
1. Open execute_report_dag.py
2. Modification line 15 to mode='reschedule'
3. Run in terminal command airflow list_dags"""
#  gave Airflow a chance to run another task while waiting for the salesdata_ready.csv file
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.sensors.file_sensor import FileSensor
from datetime import datetime

report_dag = DAG(
    dag_id = 'execute_report',
    schedule_interval = "0 0 * * *"
)

precheck = FileSensor(
    task_id='check_for_datafile',
    filepath='salesdata_ready.csv',
    start_date=datetime(2020,2,20),
    mode='reschedule' ,
    dag=report_dag
)

generate_report_task = BashOperator(
    task_id='generate_report',
    bash_command='generate_report.sh',
    start_date=datetime(2020,2,20),
    dag=report_dag
)

precheck >> generate_report_task
#|
#|
"""
\ Debugging and troubleshooting in Airflow /

  | typical ISSUES |
  
   - task won't run on schedule :
      ## check if scheduler running
       # to fix run ... in command-line
       airflow scheduler
      
      ## one schedule_interval may not passed
       # modify attribute to meet requirements
       
      ## not enough task free within executor
       # change executor type
       # add OS resourses
       # add other OSs
       # change DAG schedule
       
   - DAG won't load
      ## DAG not in Web UI
      ## DAG not in airflow list_dags
       # verify DAG is in correct folder
       # determine  DAGs folder :
       head airflow/airflow.cfg
       
   - Syntax errors
      ## DAG file won't appear
      ## diffucult to find errors in a DAG
        airflow list_dags
        python3 dagfile.py
"""
#|
#|
### DAGs in the bag
head airflow/airflow.cfg
# ANSW: The `dags_folder` is set to `/home/repl/workspace/dags`.
#|
#|
### Missing DAG
