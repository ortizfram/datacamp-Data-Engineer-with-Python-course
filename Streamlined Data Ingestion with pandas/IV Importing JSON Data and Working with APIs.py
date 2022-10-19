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
  ****************************************************************************************************"""
  
