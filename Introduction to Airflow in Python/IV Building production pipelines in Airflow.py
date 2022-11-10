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
#|
#|
### Using lists with templates
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

filelist = [f'file{x}.txt' for x in range(30)]

default_args = {
  'start_date': datetime(2020, 4, 15),
}

cleandata_dag = DAG('cleandata',
                    default_args=default_args,
                    schedule_interval='@daily')

# Modify the template to handle multiple files in a 
# single run.
templated_command = """
  <% for filename in params.filenames %>
  bash cleandata.sh {{ ds_nodash }} {{ filename }};
  <% endfor %>
"""

# Modify clean_task to use the templated command
clean_task = BashOperator(task_id='cleandata_task',
                          bash_command=templated_command,
                          params={'filenames': filelist},
                          dag=cleandata_dag)
#|
#|
### Understanding parameter options
# ANSW: Using specific tasks allows better monitoring of task state and possible parallel execution.
#|
#|
### Sending templated emails
from airflow.models import DAG
from airflow.operators.email_operator import EmailOperator
from datetime import datetime

# Create the string representing the html email content
html_email_str = """
Date: {{ ds }}
Username: {{ params.username }}
"""

email_dag = DAG('template_email_test',
                default_args={'start_date': datetime(2020, 4, 15)},
                schedule_interval='@weekly')

email_task = EmailOperator(task_id='email_task',
                           to='testuser@datacamp.com',
                           subject="{{ macros.uuid.uuid4() }}",
                           html_content=html_email_str,
                           params={'username': 'testemailuser'},
                           dag=email_dag)
#|
#|
"""
\ branching /

    > BranchPythonOperator
    > from airflow.operator.python_operator import BranchPythonOperator
    # takes a python callable to return next task_id to follow
    
    | eg: |
    
    def branch_test(**kwargs):
        if int(kwargs['ds_nodash']) % 2 ==0:
            return 'even_day_task'
        else:
            return 'odd_day_task'
            
    branch_task = BranchPythonOperator(task_id='branch_task',dag=dag,
            provide_context=True,
            python_callable=branch_test)
            
    start_tast >> branch_task >> even_day_task >> even_day_task2
    branch_task >> odd_day_task >> odd_day_task2
"""
#|
#|
### Define a BranchPythonOperator
# Create a function to determine if years are different
def year_check(**kwargs):
    current_year = int(kwargs['ds_nodash'][0:4])
    previous_year = int(kwargs['prev_ds_nodash'][0:4])
    if current_year == previous_year:
        return 'current_year_task'
    else:
        return 'new_year_task'

# Define the BranchPythonOperator
branch_task = BranchPythonOperator(task_id='branch_task', dag=branch_dag,
                                   python_callable=year_check, provide_context=True)
# Define the dependencies
branch_dag >> current_year_task
branch_dag >> new_year_task
