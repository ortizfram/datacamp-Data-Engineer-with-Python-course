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
