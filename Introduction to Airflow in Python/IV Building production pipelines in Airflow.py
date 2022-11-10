"""
Put it all together. In this final chapter, you’ll apply everything you've learned to build a production-quality workflow in Airflow.

\ Working with templates /

    > allow substituting info during DAG run
    # provide flex when defining tasks
    ## are created using 'Jinja' templating language
    
  | Templated BashOperator eg: |
    
    templated_command=''' 
        echo "Reading {{ params.filename }}"
    '''
    t1 =  BashOperator(task_id='template_taks',
            bash_command=templated_command,
            params={'filename':'file1.txt'},
            dag=example_dag)
            
    # OUT: Reading file1.txt
"""
#|
#|
### Creating a templated BashOperator
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
  'start_date': datetime(2020, 4, 15),
}

cleandata_dag = DAG('cleandata',
                    default_args=default_args,
                    schedule_interval='@daily')

# Create a templated command to execute
# 'bash cleandata.sh datestring'
templated_command='''
bash cleandata.sh {{ ds_nodash }}
'''

# Modify clean_task to use the templated command
clean_task = BashOperator(task_id='cleandata_task',
                          bash_command=templated_command,
                          dag=cleandata_dag)

