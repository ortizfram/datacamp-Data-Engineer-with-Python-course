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
***************************************************************************************"""
