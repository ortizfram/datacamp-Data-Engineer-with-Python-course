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
#````````````````````````````````````````````````````````````````````````````````````````````
"""//////////////QUERY/////////////////////////////"""
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
#`````````````````````````````````````````````````````````````````````````````````````````````
"""//////////////TRANSFORM/////////////////////////////"""
#--- Average rating per course
"""In this exercise, you'll complete a transformation function transform_avg_rating() 
that aggregates the rating data using the pandas DataFrame's .groupby() method.
The goal is to get a DataFrame with two columns, a course id and its average rating

Complete this transformation function, and apply it on raw rating data extracted via
the helper function extract_rating_data() which extracts course ratings from the rating table."""

# Complete the transformation function
def transform_avg_rating(rating_data):
    # Group by course_id and extract average rating per course
    avg_rating = rating_data.groupby('course_id').rating.mean()
    # Return sorted average ratings per course
    sort_rating = avg_rating.sort_values(ascending=False).reset_index()
    return sort_rating

# Extract the rating data into a DataFrame    
rating_data = extract_rating_data(db_engines)

# Use transform_avg_rating on the extracted data and print results
avg_rating_data = transform_avg_rating(rating_data)
print(avg_rating_data) 
#`````````````````````````````````````````````````````````````````````````````````````````````

#--- Filter out corrupt data, count null, fill null
course_data = extract_course_data(db_engines)

# Print out the number of missing values per column
#isnull()
print(course_data.isnull().sum())

# transformation: fill in the missing values
#fillna()
def transform_fill_programming_language(course_data):
    imputed = course_data.fillna({"programming_language": "R"})
    return imputed
#apply transformation to table
transformed = transform_fill_programming_language(course_data)

# Print out the number of missing values per column of transformed
print(transformed.isnull().sum())
#`````````````````````````````````````````````````````````````````````````````````````````````

#--- recommender transformation
"""to produce the final recommendations, you will use the average course ratings, and the list of eligible
recommendations per user, stored in avg_course_ratings and courses_to_recommend respectively. You will do this 
by completing the transform_recommendations() function which merges both DataFrames and finds the top 3 highest rated courses to recommend per user."""

# Complete the transformation function
def transform_recommendations(avg_course_ratings, courses_to_recommend):
    # Merge both DataFrames
    merged = courses_to_recommend.merge(avg_course_ratings) 
    # Sort values by rating and group by user_id
    grouped = merged.sort_values("rating", ascending=False).groupby("user_id")
    # Produce the top 3 values and sort by user_id
    recommendations = grouped.head(3).sort_values("user_id").reset_index()
    final_recommendations = recommendations[["user_id", "course_id","rating"]]
    # Return final recommendations
    return final_recommendations

# Use the function with the predefined DataFrame objects
recommendations = transform_recommendations(avg_course_ratings, courses_to_recommend)
#`````````````````````````````````````````````````````````````````````````````````````````````

"""//////////////SCHEDULING/////////////////////////////"""
""" put this table into a database so that it can be used by several products like a recommendation engine or an emailing system"""

#--- The target table
#connect to DB as pandas.DataFrame method 
connection_uri = "postgresql://repl:password@localhost:5432/dwh"
db_engine = sqlalchemy.create_engine(connection_uri)

#funtion to load to a Data Warehouse using .to_sql()
def load_to_dwh(recommendations):
    recommendations.to_sql("recommendations", db_engine, if_exists="replace")
#`````````````````````````````````````````````````````````````````````````````````````````````

