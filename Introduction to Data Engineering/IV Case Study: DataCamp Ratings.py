"""***************************************************************************************
Cap off all that you've learned in the previous three chapters by completing a real-world data
engineering use case from DataCamp! You will perform and schedule an ETL process that transforms
raw course rating data, into actionable course recommendations for DataCamp students!
******************************************************************************************"""

#--- Exploring the schema
"""Have a look at the diagram of the database schema of datacamp_application:
- Which column forms the relationship between the two tables?

      1 The user_id column.
      2 There is no relationship.
  ok  3 The course_id column.
      4 The combination of user_id and course_id columns."""


#--- Querying the table
"""You'll get the rating data for three sample users
and then use a predefined helper function,
print_user_comparison(), to compare the sets of course ids these users rated."""
