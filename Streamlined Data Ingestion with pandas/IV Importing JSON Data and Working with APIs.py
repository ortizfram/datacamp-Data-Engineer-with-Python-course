"""****************************************************************************************************
 Learn how to work with JSON data and web APIs by exploring a public dataset and getting cafe recommendations from Yelp.
End by learning some techniques to combine datasets once they have been loaded into data frames.
             
             - Common Web data format
             - Not tabular (unlike DataFrames)
             - Data organized into collections of objects
             - That are python dictionaries (key-values pairs)
             - Nested JSON: objects within objects
JSON = 
[{"adult_families_in_shelter":"1796","adults_in_families_with_children_in_shelter":"14607","children_in_families_with_children_in_shelter":"21314","date_of_census":"2013-08-21T00:00:00.000","families_with_children_in_shelter":"10261","individuals_in_adult_families_in_shelter":"3811","single_adult_men_in_shelter":"7231","single_adult_women_in_shelter":"2710","total_adults_in_shelter":"28359","total_children_in_shelter":"21314","total_individuals_in_families_with_children_in_shelter_":"35921","total_individuals_in_shelter":"49673","total_single_adults_in_shelter":"9941"}
,{"adult_families_in_shelter":"1803","adults_in_families_with_children_in_shelter":"14622","children_in_families_with_children_in_shelter":"21324","date_of_census":"2013-08-22T00:00:00.000","families_with_children_in_shelter":"10274","individuals_in_adult_families_in_shelter":"3827","single_adult_men_in_shelter":"7201","single_adult_women_in_shelter":"2716","total_adults_in_shelter":"28366","total_children_in_shelter":"21324","total_individuals_in_families_with_children_in_shelter_":"35946","total_individuals_in_shelter":"49690","total_single_adults_in_shelter":"9917"}
,{"adult_families_in_shelter":"1802","adults_in_families_with_children_in_shelter":"14611","children_in_families_with_children_in_shelter":"21291","date_of_census":"2013-08-23T00:00:00.000","families_with_children_in_shelter":"10266","individuals_in_adult_families_in_shelter":"3826","single_adult_men_in_shelter":"7149","single_adult_women_in_shelter":"2671","total_adults_in_shelter":"28257","total_children_in_shelter":"21291","total_individuals_in_families_with_children_in_shelter_":"35902","total_individuals_in_shelter":"49548","total_single_adults_in_shelter":"9820"}
,{"adult_families_in_shelter":"1801","adults_in_families_with_children_in_shelter":"14650","children_in_families_with_children_in_shelter":"21343","date_of_census":"2013-08-24T00:00:00.000","families_with_children_in_shelter":"10291","individuals_in_adult_families_in_shelter":"3824","single_adult_men_in_shelter":"7110","single_adult_women_in_shelter":"2690","total_adults_in_shelter":"28274","total_children_in_shelter":"21343","total_individuals_in_families_with_children_in_shelter_":"35993","total_individuals_in_shelter":"49617","total_single_adults_in_shelter":"9800"}
,{"adult_families_in_shelter":"1804","adults_in_families_with_children_in_shelter":"14694","children_in_families_with_children_in_shelter":"21400","date_of_census":"2013-08-25T00:00:00.000","families_with_children_in_shelter":"10324","individuals_in_adult_families_in_shelter":"3830","single_adult_men_in_shelter":"7230","single_adult_women_in_shelter":"2704","total_adults_in_shelter":"28458","total_children_in_shelter":"21400","total_individuals_in_families_with_children_in_shelter_":"36094","total_individuals_in_shelter":"49858","total_single_adults_in_shelter":"9934"}

 @ Reading JSON Data
   =================
        >>>>>>>>> read_json()====== takes string path to JSON, or JSON data as string
        >>>>>>>>> dtype======== kward argument to specify data type in dictionary
        >>>>>>>>> orient======== kward argument to flag uncommon JSON data layouts
    
 data/record orientation 
 ======================
             - Pandas automatically handle common orientations/ arranged
             - Pandas guesses how to arrrange it in a table
             - Consist on a list of Dictionaries, each is a table record
             
             space-efficient
             ===============
             *****column orientation =====better than record orientation 
                  - key[colum_names] : vals[list_of_vals_for_column, 1,2,3]
             >>>>>>> split----
             >>>>>>> orient
                  - key[column_name1]:[values]
                  - key[column_name2]:[values]
    
 Specifying orientation 
 ======================
 import pandas as pd
 death_causes = pd.read_json("nyc_death_causes.json",
                             orient= "split")
****************************************************************************************************"""

#--- Load JSON data
# Load pandas as pd
import pandas as pd

# Load the daily report to a dataframe
pop_in_shelters = pd.read_json("dhs_daily_report.json")

# View summary stats about pop_in_shelters
print(pop_in_shelters.describe())
"""output:
        adult_families_in_shelter  adults_in_families_with_children_in_shelter  children_in_families_with_children_in_shelter  families_with_children_in_shelter  \
count                   1000.000                                     1000.000                                       1000.000                           1000.000   
mean                    2074.955                                    16487.932                                      23273.873                          11588.835   
std                      148.020                                      848.364                                        926.244                            626.414   
min                     1796.000                                    14607.000                                      21291.000                          10261.000   
25%                     1906.000                                    15831.500                                      22666.000                          11060.000   
50%                     2129.000                                    16836.000                                      23285.500                          11743.000   
75%                     2172.250                                    17118.250                                      23610.000                          12146.000   
max                     2356.000                                    17733.000                                      25490.000     """
  #``````````````````````````````````````````````````````````````````````````````````````````````````````

#---Work with JSON orientations
try:
    # Load the JSON with orient specified
    df = pd.read_json("dhs_report_reformatted.json",
                      orient= "split")
    
    # Plot total population in shelters over time
    df["date_of_census"] = pd.to_datetime(df["date_of_census"])
    df.plot(x="date_of_census", 
            y="total_individuals_in_shelter")
    plt.show()
    
except ValueError:
    print("pandas could not parse the JSON.")
  
  """---without orient kward, pipeline wouldn't throw a graph"""\
  #``````````````````````````````````````````````````````````````````````````````````````````````````````

 """****************************************************************************************************
 @ Intro to APIs
   =============
   web application programming interfaces, most common source of JSON data.
         - Defines how an app communicates with other programs
         - Get data from app without having to know app db architecture
         $$ it's like using a catalog to order products
         - API provides endpoint to send requests to 
         
         Requests (Requests Library)
         ===========================
           - Requests and sends data from any URL
           - Not tied to any particular API
           
           >>>>>>>>> requests.get(url_string) ===== get data from URL/ retrieve data
           >>>>>>>>> params  (kward)====== takes dictionary of parameter names and values To customize request
           >>>>>>>>> headers  (kward)====== takes dictionary, can be used to provide User Authentication to API
           - Result: Response Object, containing data and metadata 
           >>>>>>>>> response.json() ====== to get just the JSON data--- returns Dictionary
           <-- read_json()=== expects Strings, not Dictionaries
           <-- pd.DataFrame() ====== Load the response JSON to a df.---read_json()--> will give an error
           
              Yelp (Business Search API)
              ==========================
              - makes busines's reviews/ratings data available via its APIs
 Making requests
 ===============
 import requests
 import pandas as pd
 
 # Create variable for API endpoint
 api_url = "https://api.yelp.com/v3/businesses/search"
 
 # Set up parameter Dictionary according documentation
 params = {"term" : "bookstore",
           "location" : "San Francisco"}
           
 # Set up header Dictionary w/ API key according documentation
 headers = {"Authorization" : "Bearer {}".format(api_key)}
 
 # Call API
 response = requests.get(api_url,
                         params=params,
                         headers=headers)
  
Parsing responses
=================
# Isolate JSON data from response object
data = response.json()
print(data)
# returns tictionary

# Load business to df
bookstores = pd.DataFrame(data["businesses"])
print(bookstores.head(2))
 ****************************************************************************************************"""
 
 #--- Get data from an API
api_url = "https://api.yelp.com/v3/businesses/search"

# Get data about NYC cafes from the Yelp API
response = requests.get(api_url, 
                headers=headers, 
                params=params)

# Extract JSON data from the response
data = response.json()

# Load data to a dataframe
cafes = pd.DataFrame(data["businesses"])

# View the data's dtypes
print(cafes.dtypes)
"""output:
id                object
alias             object
name              object
image_url         object
is_closed           bool
url               object
review_count       int64
categories        object
rating           float64
coordinates       object
transactions      object
location          object
phone             object
display_phone     object
distance         float64
price             object"""
  #``````````````````````````````````````````````````````````````````````````````````````````````````````
 
#--- Set API parameters
# Create dictionary to query API for cafes in NYC
parameters = {"term" : "cafe",
          	  "location" : "NYC"}

# Query the Yelp API with headers and params set
response = requests.get(api_url,
                headers=headers,
                params=parameters)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a dataframe and print head
cafes = pd.DataFrame(data["businesses"])
print(cafes.head())
"""output:
   phone   display_phone  distance price  
0                                1856.127   NaN  
1  +17182856180  (718) 285-6180  2087.817    $$  
2  +12122287888  (212) 228-7888  2435.843    $$  
3  +16465246353  (646) 524-6353  1657.233     $  
4  +17188018037  (718) 801-8037   635.782    $$  """
  #``````````````````````````````````````````````````````````````````````````````````````````````````````

#--- Set request headers
# Create dictionary that passes Authorization and key string
headers = {"Authorization": "Bearer {}".format(api_key)}

# Query the Yelp API with headers and params set
response = requests.get(api_url,
                        headers=headers,
                        params=params)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a dataframe and print names
cafes = pd.DataFrame(data["businesses"])
print(cafes.name)
"""output:
0             Coffee Project NY
1                Urban Backyard
2              Saltwater Coffee
3                 Bird & Branch
4                  Bibble & Sip
5             Coffee Project NY
6                        Burrow
7                   Cafe Patoro
8                     Sweatshop
9                       Round K
10               Kobrick Coffee
11            Kaigo Coffee Room
12              Absolute Coffee
13                     Devocion
14                The Uncommons
15                      Butler 
16              Cafe Hanamizuki
17    Brooklyn Roasting Company
18             Takahachi Bakery
19              Happy Bones NYC
Name: name, dtype: object"""
#``````````````````````````````````````````````````````````````````````````````````````````````````````
"""****************************************************************************************************
Nested JSON (restructuring)
============================
 - JSON contains objects w/ {attribute/value pairs}
 - Nested when values itself is an object
 
     >>>>>>>> pandas.io.json ---(pd.submodule)
     <->>>>>> json_normalize()======function to flatten nested JSONs.---takes Dict,[{}]----return DF
     >>>>>>>> attribute.nestedattribute==== DEFAULT flattened column name pattern
     >>>>>>>> sep ===== choose different separator
    
LOADING Nested JSON data
========================

import pandas as pd
import requests
from pandas.io.json import json_normalize

# Create var for API endpoint, headers, params
api_url = "https://api.yelp.com/v3/businesses/search"
headers = {"Authorize" : "Bearer {}".format(api_key)}
params = {"terms" : "bookstore",
          "location" : "San Francisco"}
          
# Make API call , Extract JSON data 
response = requests.get(api_url,
                        headers=headers,
                        params = params)
data = response.json()

# Flatten data and load to df, with _ separators
bookstores = json_normalize(data["businesses"], sep = "_")
print(list(bookstores))
 
 DEEPLY Nested data
===================
   >>>>>>>> json_normalize()
        >>>>>>>> record_path ====== String/List of String Attributes To Nested data
        >>>>>>>> meta ====== list of attributes to load to df
        >>>>>>>> meta_prefix ===== (diffenciate columns) string to prefix to meta column names
        
   # Flatten categories data, bring in business details 
   df = json_normalize(data["businesses"],
                       sep = "_",
                       record_path ="categories",
                       meta = ["name",
                               "alias",
                               "rating",
                               ["coordinates", "latitude"],
                               ["coordinates", "longitude"]],
                       meta_prefix ="biz_")
                       # <-- business and categories have both alias column, so set a meta_prefix to differentiate
 ****************************************************************************************************"""

#--- Flatten nested JSONs
"""Your job is to flatten out the next level of data in the coordinates and location columns."""
# Load json_normalize()
from pandas.io.json import json_normalize

# Isolate the JSON data from the API response
data = response.json()

# Flatten business data into a dataframe, replace separator
cafes = json_normalize(data["businesses"],
                     sep="_")

# View data
print(cafes.head())
"""output:
 location_display_address price  
0        [71 Smith St, Brooklyn, NY 11201]   NaN  
1  [276 Livingston St, Brooklyn, NY 11201]    $$  
2       [239 E 5th St, New York, NY 10003]    $$  
3     [116 Suffolk St, New York, NY 10002]     $  
4       [163 Plymouth St, Dumbo, NY 11201]    $$ """
#``````````````````````````````````````````````````````````````````````````````````````````````````````

#--- Handle deeply nested data 1
# Flatten businesses records and set underscore separators
flat_cafes = json_normalize(data["businesses"],
                  sep="_")

# View the data
print(flat_cafes.head())
#``````````````````````````````````````````````````````````````````````````````````````````````````````

#--- Handle deeply nested data 2
# Specify record path to get categories data
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path= "categories")

# View the data
print(flat_cafes.head())
"""output:
           alias              title
0            coffee       Coffee & Tea
1            coffee       Coffee & Tea
2  coffeeroasteries  Coffee Roasteries
3             cafes              Cafes
4            coffee       Coffee & Tea"""
#``````````````````````````````````````````````````````````````````````````````````````````````````````

#--- Handle deeply nested data 3
# Load other business attributes and set meta prefix
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path="categories",
                    		meta=["name", 
                                  "alias",  
                                  "rating",
                          		  ["coordinates", "latitude"], 
                          		  ["coordinates", "longitude"]],
                    		meta_prefix="biz_")

# View the data
print(flat_cafes.head())
"""output:
       alias              title           biz_name                   biz_alias         biz_rating biz_coordinates_latitude biz_coordinates_longitude
0            coffee       Coffee & Tea        White Noise      white-noise-brooklyn-2        4.5                   40.689                   -73.988
1            coffee       Coffee & Tea           Devocion         devocion-brooklyn-3        4.0                   40.689                   -73.983
2  coffeeroasteries  Coffee Roasteries           Devocion         devocion-brooklyn-3        4.0                   40.689                   -73.983
3             cafes              Cafes           Devocion         devocion-brooklyn-3        4.0                   40.689                   -73.983
4            coffee       Coffee & Tea  Coffee Project NY  coffee-project-ny-new-york        4.5  """

"""****************************************************************************************************

Combining multiple datasets
===========================
Pandas method for combining data sets

        Appending
        =========
        Use case: adding rows to other df
        
          >>>>>>> append() (df method) ==== takes df to add on as argument
          >>>>>>> ignore_index = True   (append argument)==== to renumber rows

        # Get first 20 bookstore results
        #*1
        params = {"term" : "bookstore",
                  "location" : "San Francisco"}
                  
        first_results = requests.get(api_url,
                                    headers=headers
                                    params=params).json()
        
       first_20_bookstores = json_normalize(firs_results["businesses"],
                                            sep="_") 
                                            
       print(first_20_bookstores.shape)   
       #(20, 24)
       #*1 
       # Get next 20
       params["offset"] = 20
       
       # put both together
       bookstores = first_20_bookstores.append(next_20_bookstores,
                                               ignore_index=True)
       print(bookstores.name)
       
       Merging
       =========
       USe case: adding related columns
         - datasets have key colum(s) w/ common values, like SQL joins
         - key columns should be same d.type to merge 
         
         >>>>>>> merge()==== (pandas) version of SQL JOIN---takes name of other df--srt of columns to merge on
         >>>>>>> ON==== (pandas) specifty column match in both df
         >>>>>>> left_on..right_on==== (pandas) if key_names differ
         
         # Merge weather into call_counts on date column
         merged = call_count.merge(weather,
                                   left_on="created_date",
                                   right_on="date")
****************************************************************************************************"""
