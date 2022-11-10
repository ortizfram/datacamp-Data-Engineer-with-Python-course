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

