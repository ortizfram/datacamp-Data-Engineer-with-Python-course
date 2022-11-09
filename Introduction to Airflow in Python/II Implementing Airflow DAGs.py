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
