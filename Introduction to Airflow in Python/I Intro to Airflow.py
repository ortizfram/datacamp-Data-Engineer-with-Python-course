"""
complete introduction to the components of Apache Airflow and learn how and why you should use them.

\ workflow /

  > set of steps to accomplish a d.e task
    ..such as -downloading files -copying data -filtering info -writing to a database
  > of varying leves of complexity

\ airflow /

  > platform to program workflows 
    - creating
    - scheduling
    - monitoring
    
    > can implement any language, but workflows written : in Python 
    > implement workflows as DAGs : Direct Acyclic Graphs
    > access via: code, command-line, web interface 
    
    | DAG simple definition eg: |
    
      etl_dag = DAG(
            dag_id = 'etl_pipeline',
            default_args = {"start_data":"2020-01-08"}
            )
      ------
            
    | Run a workflow in Airflow eg: |
    
    airflow run <dag_ig> <task_id> <start_date>
    airflow run example_etl download-file 2020-01-10
    -------
"""
#|
#|
### Running a task in Airflow
"""-Which command would you enter in the console to run the desired task?"""
airflow run etl_pipeline download_file 2020-01-08
#|
#|
### Examining Airflow commands
"""-Which of the following is NOT an Airflow sub-command?

    | get airflow documentation ariflow description |
    
    airflow -h
    
-list_dags
-edit_dag
-test
-scheduler
"""
# Answ: edit_dag
#|
#|
"""
\ What's a DAG /

  > Direct : flow representing dependencies
  > Acyclic : do not loop
  > Graph : actual set of components
  
    # written in python, components in any language
    # made up of components : tasks to be executed (operators, sensors)
    # dependencies defined (explicit or implicit)
    
    | Define a DAG eg:|
    
    from airflow.models import DAG
    from datetime import datetime
    
    default_arguments = {
      'owner' : 'jdoe',
      'emial' : 'jdoe@datacamp.com',
      'start_date' : datetime(2020, 1, 20)
    }
    
    etl_dag = DAG( 'etl_workflow', default_args=default_arguments )
    ---------
"""
#|
#|
### Defining a simple DAG
"""1/3"""
# Import the DAG object
from airflow.models import DAG
#|
"""2/3"""
# Import the DAG object
from airflow.models import DAG

# Define the default_args dictionary
default_args = {
  'owner': 'dsmith',
  'start_date': datetime(2020, 1, 14),
  'retries' : 2
}
#|
"""3/3"""
# Import the DAG object
from airflow.models import DAG

# Define the default_args dictionary
default_args = {
  'owner': 'dsmith',
  'start_date': datetime(2020, 1, 14),
  'retries': 2
}

# Instantiate the DAG object
etl_dag = DAG( 'example_etl', default_args= default_args)
#|
#|
### Working with DAGs and the Airflow shell
"""-How many DAGs are present in the Airflow system from the command-line?
    
    | list DAGs inshell |
    
    airflow list_dags
"""
airflow list_dags
# Answ: 2
#|
#|
### Troubleshooting DAG creation
"""Instructions

Use the airflow shell command to determine which DAG is not being recognized correctly.
After you determine the broken DAG, open the file and fix any Python errors.
Once modified, verify that the DAG now appears within Airflow's output."""
airflow list_dags
----------
from airflow.models import DAG # fixed part
default_args = {
  'owner': 'jdoe',
  'email': 'jdoe@datacamp.com'
}
dag = DAG( 'refresh_data', default_args=default_args )
#|
#|
"""
\ Airflow web interface /
.
"""
#|
#|
### Airflow web interface

  
