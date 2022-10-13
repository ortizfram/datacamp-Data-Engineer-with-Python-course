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

# Complete the connection URI () #(postgresql)
connection_uri = "postgresql://repl:password@localhost:5432/datacamp_application" #database_name last /
#create engine
db_engine = sqlalchemy.create_engine(connection_uri) 


# Get user with id 4387 #(pd.read_sql)
user1 = pd.read_sql("SELECT * FROM rating WHERE user_id = 4387", db_engine)

# Get user with id 18163
user2 = pd.read_sql("SELECT * FROM rating WHERE user_id = 18163", db_engine)

# Get user with id 8770
user3 = pd.read_sql("SELECT * FROM rating WHERE user_id = 8770", db_engine)

# Use the helper function to compare the 3 users
print_user_comparison(user1, user2, user3)
"""output:
Course id overlap between users:
================================
User 1 and User 2 overlap: {32, 96, 36, 6, 7, 44, 95}
User 1 and User 3 overlap: set()
User 2 and User 3 overlap: set()"""


#--- Average rating per course
"""In this exercise, you'll complete a transformation function transform_avg_rating() 
that aggregates the rating data using the pandas DataFrame's .groupby() method.
The goal is to get a DataFrame with two columns, a course id and its average rating

Complete this transformation function, and apply it on raw rating data extracted via
the helper function extract_rating_data() which extracts course ratings from the rating table."""

