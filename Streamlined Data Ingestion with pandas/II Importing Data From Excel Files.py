"""***************************************************************************************
[] Spreadsheets:
         - Unlike flatfiles, Can have Formatting and Formulas
         - MUltiple spreadsheets can exist in a workbook
         - load them all >>>>>>>> read_excel()
         $$$ if is important info, export without formatting cause Pandas does not import spreadsheet formatting 
         
   Loading Spreadsheets XLSX:
=========================
          import pandas as pd
          # Read excel file
          survey_data = pd.read_excel("fcc_survey.xlsl")
          #view first 5 lines
          print(survey_data.head())
          
Modifiying imports:
=========================          
           >>>>>>>>> nrows--------- select how many rows to load
           >>>>>>>>> skiprows------accepts a list of row n, funtion to filter rows to skip
           >>>>>>>>> usecols------- chooose columns by name, position number, letter, funtion, RANGES
           
           # read columns & skipping meta headers
           survey_data = pd.read_excel("fcc_survey.xlsl", 
                                        skiprows=2,
                                        usecols= "W:AB, AR")
***************************************************************************************"""

#--- Get data from a spreadsheet
# Load pandas as pd
import pandas as pd

# Read spreadsheet and assign it to survey_responses
survey_responses = pd.read_excel("fcc_survey.xlsx")

# View the head of the dataframe
print(survey_responses.head())
#```````````````````````````````````````````````````````````````````````````````````````````````

#--- Load a portion of a spreadsheet
# Create string of lettered columns to load
col_string = "AD, AW:BA"

# Load data with skiprows and usecols set
survey_responses = pd.read_excel("fcc_survey_headers.xlsx", 
                        skiprows=2, 
                        usecols= col_string)

# View the names of the columns selected
print(survey_responses.columns)
#```````````````````````````````````````````````````````````````````````````````````````````````
"""***************************************************************************************
Getting data from multiple worksheets
========================= pd
           >>>>>>>>> read_excel()--------- loads first sheet 
           >>>>>>>>> sheet_name--------- load other sheets (sheet_name/[sheet_name_list]/ position zero-index) in the read argument
           >>>>>>>>> sheet_name = None--------- read all sheets in workbook. returns a Dict where keys are sheetnames

           
           #Get data from 2nd sheet 2017 data
           survey_data_sheet2 = pd.read_excel("fcc_survey.xslx", sheetname = 1)
           survey_data_sheet2 = pd.read_excel("fcc_survey.xslx", sheetname = "2017")
           
           #Get all data from workbook all sheets
           survey_data_sheet2 = pd.read_excel("fcc_survey.xslx", sheetname = None)   
***************************************************************************************"""

#---Select a single sheet 1== providing sheet index
#plot of job Dev. job preferences in 2017
# Create df from second worksheet by referencing its position, 2016 was already done
responses_2017 = pd.read_excel("fcc_survey.xlsx",
                               sheet_name= 1)

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()
"""people prefer working for a medium size company over anythin else, followed by own business"""
#```````````````````````````````````````````````````````````````````````````````````````````````

#---Select a single sheet 2 ==providing sheet name
#plot of job Dev. job preferences in 2017
# Create df from second worksheet by referencing its name
responses_2017 = pd.read_excel("fcc_survey.xlsx",
                               sheet_name= "2017")

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()
#```````````````````````````````````````````````````````````````````````````````````````````````

#---Select multiple sheets 1=== sheet_name a list of names
# Load both the 2016 and 2017 sheets by name
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name=['2016','2017'])

# View the data type of all_survey_data
print(type(all_survey_data))
#```````````````````````````````````````````````````````````````````````````````````````````````
#---Select multiple sheets 2=== sheet_name a list[index, name]
# Load all sheets in the Excel file
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name= [0,"2017"])

# View the sheet names in all_survey_data
print(all_survey_data.keys())
#```````````````````````````````````````````````````````````````````````````````````````````````
#---Select multiple sheets 3=== all whitout listing
# Load all sheets in the Excel file
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name= None)

# View the sheet names in all_survey_data
print(all_survey_data.keys())
#```````````````````````````````````````````````````````````````````````````````````````````````

#---Work with multiple spreadsheets === compile similar spreadsheets into one dataset.
# Create an empty dataframe
all_responses = pd.DataFrame()

# Set up for loop to iterate through values in responses
for df in responses.values():
  # Print the number of rows being added
  print("Adding {} rows".format(df.shape[0]))
  # Append df to all_responses, assign result
  all_responses = all_responses.append(df)

# Graph employment statuses in sample
counts = all_responses.groupby("EmploymentStatus").EmploymentStatus.count()
counts.plot.barh()
plt.show()
"""***************************************************************************************
Modifying imports: true/false data  bools
==================================
           >>>>>>>>> bootcamp_data.sum()--------- count True values
           >>>>>>>>> bootcamp_data.isna().sum()--------- count NAs
           >>>>>>>>> dtype={}--------- specify boolean columns in argument
                  bool_data = pd.read_excel("fcc_survey_booleans.xlsx", dtype= {column_name : bool}) 
setting custom True/False values
================================== 
           >>>>>>>>> true_values=["Yes"]
           >>>>>>>>> false_values=["No"]
                  # load data with Boolean dtypes and custom T/F values
                  bool_data = pd.read_excel("fcc_survey_booleans.xlsx", dtype= {column_name : bool,
                                                                                 AttendBootcamp : bool},
                                                                                 true_values= ["Yes"],
                                                                                 false_values= ["No"])
****************************************************************************************"""
                  
#---Set Boolean columns 1 === count NAs in each column
"""Note which columns besides ID.x, if any, have zero NAs."""
# Load the data
survey_data = pd.read_excel("fcc_survey_subset.xlsx")

# Count NA values in each column
print(survey_data.isna().sum())

"""output:
ID.x                        0
HasDebt                     0
HasFinancialDependents      7
HasHomeMortgage           499
HasStudentDebt            502
dtype: int64"""
#```````````````````````````````````````````````````````````````````````````````````````````````
