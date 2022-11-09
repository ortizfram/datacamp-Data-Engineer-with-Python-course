"""
basics of implementing Airflow DAGs. Through hands-on activities, you’ll learn how to set up and deploy operators, tasks, and scheduling.

\ Airflow operators /

  # represent a single task in a workflow
  # run independently (usually)
  # Do NOT share info
  # Various opps to perform diff tasks
  
  | Bash Operator types |
  
  BashOperator(
      task_id='bash_example',
      bash_command='echo "Example!"',
      dag=ml_dag
  )
  
  BashOperator(
      task_id='bash_script_example',
      bash_command='runcleanup.sh',
      dag=ml_dag
  )
  
  | Bash Operator egs: |
  
  #import Bash op
  from airflow.operators.bash_operator import BashOperator
  
  example_task= BashOperator(
      task_id='bash_ex',
      bash_command='echo 1',
      dag=dag                 # asign op to the dag
  )
  
  ## quick data cleaning op using cat & awk
  bash_task = BashOperator(task_id='clean_addresses',
                  bash_command='cat addresses.txt | awk "NF==10 > cleaned.txt"',  # awk equals cut
                  dag=dag
                  )
"""
#|
#|
### Defining a BashOperator task
# Import the BashOperator
from airflow.operators.bash_operator import BashOperator

# Define the BashOperator 
cleanup = BashOperator(
    task_id='cleanup_task',
    # Define the bash_command
    bash_command='cleanup.sh',
    # Add the task to the dag
    dag=analytics_dag
)
#|
#|
### Multiple BashOperators
# Define a second operator to run the `consolidate_data.sh` script
consolidate = BashOperator(
    task_id='consolidate_task',
    bash_command='consolidate_data.sh',
    dag=analytics_dag)

# Define a final operator to execute the `push_data.sh` script
push_data = BashOperator(
    task_id='pushdata_task',
    bash_command='push_data.sh',
    dag=analytics_dag)
#|
#|
"""
\ Airflow tasks /

  >>>>>> upstream :before
  >>>>>> downstream : after
  
    | set upstream or downstream tasks |
    
    task1 << task2  
    # means: task1 => downstream task2
    task1 >> task2  
    # means: task1 => upstream task2 
"""
#|
#|
### Define order of BashOperators
# Define a new pull_sales task
pull_sales = BashOperator(
    task_id='pullsales_task',
    bash_command='wget https://salestracking/latestinfo?json',
    dag=analytics_dag
)

# Set pull_sales to run prior to cleanup
pull_sales >> cleanup

# Configure consolidate to run after cleanup
consolidate << cleanup

# Set push_data to run last
consolidate >> push_data
#|
#|
### Determining the order of tasks
"""which order the defined tasks run. The code in question shows the following:
pull_data << initialize_process
pull_data >> clean >> run_ml_pipeline
generate_reports << run_ml_pipeline"""
# ANSW: init, pull, clean, run pipe, report 
#|
#|
### Troubleshooting DAG dependencies
"""
List the DAGs.
Decipher the error message.
Use cat workspace/dags/codependent.py to view the Python code.
Determine which of the following lines should be removed from the Python code. You may want to consider the last line of the file."""
airflow list_dags
cat workspace/dags/codependent.py
# ANSW: task3 >> task1 #should be removed
#|
#|
"""
\ Additional operators /

    | PythonOperator eg: |
    
    from airflow.operatosr.python_operators import PythonOperator
    
    def printme():
        print("This goes in logs")
    
    python_task=PythonOperator(
        task_id='simple_print',
        python_callable=printme,
        dag=example_dag
    )
   
\ Arguments /

  # supports to tasks
    -positional
    -keyword
  
  | op_kwargs eg: |
  
  def sleep(lenght_of_time):
      time.sleep(lenght_of_time)
      
  sleep_task = PythonOperator(
      task_id='sleep',
      python_callable=sleep,
      op_kwargs={'lenght_of_time':5},
      dag=example_dag
  )
"""
#|
#|
### Using the PythonOperator
# Define the method
def pull_file(URL, savepath):
    r = requests.get(URL)
    with open(savepath, 'wb') as f:
        f.write(r.content)    
    # Use the print method for logging
    print(f"File pulled from {URL} and saved to {savepath}")
    
# Import the PythonOperator class
from airflow.operators.python_operator import PythonOperator

# Create the task
pull_file_task = PythonOperator(
    task_id='pull_file',
    # Add the callable
    python_callable=pull_file,
    # Define the arguments
    op_kwargs={'URL':'http://dataserver/sales.json', 'savepath':'latestsales.json'},
    dag=process_sales_dag
)
#|
#|
### More PythonOperators
# Add another Python task
parse_file_task = PythonOperator(
    task_id='parse_file',
    # Set the function to call
    python_callable=parse_file,
    # Add the arguments
    op_kwargs={'inputfile':'latestsales.json', 'outputfile':'parsedfile.json'},
    # Add the DAG
    dag=process_sales_dag
)
#|
#|
### EmailOperator and dependencies
# Import the Operator
from airflow.operators.email_operator import EmailOperator

# Define the task
email_manager_task = EmailOperator(
    task_id='email_manager',
    to='manager@datacamp.com',
    subject='Latest sales JSON',
    html_content='Attached is the latest sales JSON file as requested.',
    files='parsedfile.json',
    dag=process_sales_dag
)

# Set the order of tasks
pull_file_task >> parse_file_task >> email_manager_task
#|
#|
"""
\ airflow scheduling /
    
    | schedule_interval |
    
      special presets:
          - None : don't schedule ever, only manually triggered
          - @once : schedule inly once
    
      | mantain state of workflows |
    
        - runing
        - failed
        - success

\ schedule attributes /

    > start_data
    > end_date
    > max_tries : how many attemps?
    > schedule_interval : how often to run?
    
    | CRON style syntax |
    
    
      *** How to time a cron job : 
                * minute (0-59)
                ** hour (0-23)
                *** day of month  (1-31)
                **** month  (1-12)
                ***** day of week (1-7) (0 is Sunday)
                
                @hourly
                @daily
                @weekly
"""
#|
#|
### Schedule a DAG via Python
# Update the scheduling arguments as defined
default_args = {
  'owner': 'Engineering',
  'start_date': datetime(2019, 11, 1),
  'email': ['airflowresults@datacamp.com'],
  'email_on_failure': False,
  'email_on_retry': False,
  'retries': 3,
  'retry_delay': timedelta(minutes=20)
}

# Use the cron syntax to configure a schedule of every Wednesday at 12:30pm.
dag = DAG('update_dataflows', default_args=default_args, schedule_interval='30 12 * * 3')
#|
#|
### Deciphering Airflow schedules
"""understand exactly how intervals relate to each other, whether it's a cron format, timedelta object, or a preset.
-Order the schedule intervals from least to greatest amount of time."""
# ANSW: (least to most) 
# *****, timedelta(minutes=5), @hourly, * 0,12 * * *, timedelta(days=1), @weekly
#|
#|
### Troubleshooting DAG runs
# ANSW: The `schedule_interval` has not yet passed since the `start_date`.
