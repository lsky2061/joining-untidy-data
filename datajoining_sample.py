#Work sample for Luke Corwin

#Use pandas for data set manipulation and merger
import pandas as pd

#### This program written to satisfy the following prompt ####

#Using any software (commercial and open source) you like, programmatically join the following two untidy sample datasets:
#DOT Licensed drivers--Ratio of licensed drivers to population -
## https://www.fhwa.dot.gov/policyinformation/statistics/2014/xls/dl1c.xls.
#DOT Licensed Drivers by State, Sex, and Age Group
## https://www.fhwa.dot.gov/policyinformation/statistics/2014/xls/dl22.xls.
####

#Four sheets from the Excel files total; load each as a separate dataframe.

#First, the males from Table DL-22
dl22_M = pd.read_excel("dl22.xls",sheet_name="MALES",
                       skiprows=[0,1,2,3,4,5,6,7,8,9,10,11,12],
                       index_col=None,usecols="A:Q,T:AC",header=0)

#For each sheet, we need unique column names
col_names_M = ["State", "Males 19 and Under", "Males 20-24", "Males 25-29",
               "Males 30-34", "Males 35-39", "Males 40-44", "Males 45-49",
               "Males 50-54", "Males 55-59", "Males 60-64", "Males 65-69",
               "Males 70-74", "Males 75-79", "Males 80-84",
               "Males 85 and Over",
               "Total Licensed Male Drivers (Table DL-22)",
               "Males under 16", "Males 16", "Males 17", "Males 18",
               "Males 19", "Males 20", "Males 21", "Males 22",
               "Males 23", "Males 24"]

dl22_M.columns = col_names_M


#Female Drivers
dl22_F = pd.read_excel("dl22.xls",sheet_name="FEMALES",
                       skiprows=[0,1,2,3,4,5,6,7,8,9,10,11,12,66,67,68,69],
                       index_col=None,usecols="A:Q,T:AC",header=0)

col_names_F = ["State", "Females 19 and Under", "Females 20-24",
               "Females 25-29", "Females 30-34", "Females 35-39",
               "Females 40-44", "Females 45-49", "Females 50-54",
               "Females 55-59", "Females 60-64", "Females 65-69",
               "Females 70-74", "Females 75-79", "Females 80-84",
               "Females 85 and Over",
               "Total Licensed Female Drivers (Table DL-22)", "Females under 16",
               "Females 16", "Females 17", "Females 18", "Females 19",
               "Females 20", "Females 21", "Females 22", "Females 23",
               "Females 24"]

dl22_F.columns = col_names_F

#Total Drivers
dl22_T = pd.read_excel("dl22.xls",sheet_name="TOTAL",
                       skiprows=[0,1,2,3,4,5,6,7,8,9,10,11,12,
                                 66,67,68,69,70,71,72,73,74,75,76,77],
                       index_col=None,usecols="A:Q,T:AC",header=0)

col_names_T = ["State", "Total 19 and Under", "Total 20-24", "Total 25-29",
               "Total 30-34", "Total 35-39", "Total 40-44", "Total 45-49",
               "Total 50-54", "Total 55-59", "Total 60-64", "Total 65-69",
               "Total 70-74", "Total 75-79", "Total 80-84",
               "Total 85 and Over", "Total Licensed Drivers (Table DL-22)",
               "Total under 16", "Total 16", "Total 17", "Total 18",
               "Total 19", "Total 20", "Total 21", "Total 22", "Total 23",
               "Total 24"]

dl22_T.columns = col_names_T

#This bit is to keep the text from overrunning
#the edge of the page in my documentation
rn = "Ratio of Licensed Drivers to "
rn += "Private and Commercial Motor Vehicles Registered"

#Read in Table DL-1C
dl1c = pd.read_excel("dl1c.xls",skiprows=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,
                                          66,67,68,69],
                     usecols="A:M",header=None)

col_names_D = ["State","Licensed Male Drivers (Table DL-1C)",
               "Percent Male Drivers of Total",
               "Licensed Female Drivers (Table DL-1C)",
               "Percent Female Drivers of Total",
               "Total Licensed Drivers (Table DL-1C)",
               rn,
               "Total Resident Population",
               "Male Driving Age Population (16 and Over)",
               "Female Driving Age Population (16 and Over)",
               "Total Driving Age Population (16 and Over)",
               "Drivers Per 1000 Total Resident Population",
               "Drivers per 1000 Driving Age Population"]

dl1c.columns = col_names_D

#Clean up state names so that they have uniform values among the four sheets
dl1c['State'] = dl1c['State'].str.replace('[0-9,/]','')
dl1c['State'] = dl1c['State'].str.strip()

#Merge the three sheets from Table DL-22 togther
merged_table = pd.merge(dl22_M,dl22_F,how='left',on='State')
merged_table = pd.merge(merged_table,dl22_T,how='left',on='State')

#Clean up the state names for Table DL-22
#so they have the same values as Table DL-1C
merged_table['State'] = merged_table['State'].str.replace('[0-9,/]','')
merged_table['State'] = merged_table['State'].str.strip()

#Merge DL-22 with DL-1C using the state column as the common column
merged_table = pd.merge(merged_table,dl1c,how='left',on='State')

print(merged_table.describe)
#Export merged dataset to .csv file for screenshots and future use
merged_table.to_csv("DataJoinSample.csv")

