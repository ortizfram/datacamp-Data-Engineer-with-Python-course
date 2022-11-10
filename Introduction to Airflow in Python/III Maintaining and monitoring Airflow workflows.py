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
        mode='rechedule' : 'give task slot and try again'
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