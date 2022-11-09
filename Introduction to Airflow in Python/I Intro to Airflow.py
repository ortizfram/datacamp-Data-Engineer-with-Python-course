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
            
    | Run a workflow in Airflow |
    
    airflow run <dag_ig> <task_id> <start_date>
    airflow run example_etl download-file 2020-01-10
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

    | get airflow documentation |
    
    airflow -h
    
-list_dags
-edit_dag
-test
-scheduler
"""
# Answ: edit_dag
