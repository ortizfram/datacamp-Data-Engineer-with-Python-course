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
#|
#|
### Templates with multiple arguments
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
  'start_date': datetime(2020, 4, 15),
}

cleandata_dag = DAG('cleandata',
                    default_args=default_args,
                    schedule_interval='@daily')

# Modify the templated command to handle a
# second argument called filename.
templated_command = """
  bash cleandata.sh {{ ds_nodash }} {{ params.filename }}
"""

# Modify clean_task to pass the new argument
clean_task = BashOperator(task_id='cleandata_task',
                          bash_command=templated_command,
                          params={'filename': 'salesdata.txt'},
                          dag=cleandata_dag)

# Create a new BashOperator clean_task2
clean_task2 = BashOperator(task_id='cleandata_task2',
                           bash_command=templated_command,
                           params={'filename':'supportdata.txt'},
                           dag=cleandata_dag)
                           
# Set the operator dependencies
clean_task2 << clean_task
#|
#|
"""
\ more advanced templates /

    | eg: |

        templated_command = '''
        {% for filename in params.filenames %}
            echo "Reading {{filename}}"
        {% endfor %}
        '''

        t1= BashOperator(task_id='template_task',
                  bash_command=templated_command,
                  params={'filenames':['file1.txt','file2.txt']},
                  dag=example_dag)

    | variables |
    
        > Execution date: 
             {{ ds }}
        > Execution date, no dashes: 
             {{ ds_nodash }}
        > Previous execution date: 
             {{ prev_ds }}
        > Prev execution date no dashes:
             {{ prev_ds_nodash }}
        > DAG object : 
             {{ dag }}
        > airflow config object:
             {{ conf }}
    
    | Macros |
    
        > {{ macros.datetime }}
        > {{ macros.timedelta }}
        > {{ macros.uuid }}
        > {{ macros.ds_add('2020-04-15', 5) }}  : modify days from date,  RETURNS: 2020-04-20
"""
