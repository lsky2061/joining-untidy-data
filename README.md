# joining-untidy-data

This repository was created in response to a work sample prompt to evaluate my skills in cleaining and joining untidy data sets. The prompt is as follows:


Using any software (commercial and open source) you like, programmatically join the following two untidy sample datasets:

DOT Licensed drivers--Ratio of licensed drivers to population -https://www.fhwa.dot.gov/ policyinformation/statistics/2014/xls/dl1c.xls.

DOT Licensed Drivers by State, Sex, and Age Group - https://www.fhwa.dot.gov/policyinformation/statistics/2014/xls/dl22.xls.

I have committed these Excel files in the repository for ease of reproducing my work.

I joined these datasets using Python and pandas, specifically the pandas merge function.  I read each sheet from the excel files into a separate pandas data frame. By including only the relevant columns and rows while reading the data in, I excluded the columns and rows that were blank, contained extraneous entries, or did not contain tabular data. Alternatively, one could read in all data and eliminate columns and rows based on relevant conditions.  

Column names were not always in the same row and were identical among certain sheets, so I created distinct and descriptive names for each column in each of the four sheets. Where multiple columns contained what should be the same information, I decided to keep them all (with distinct names) so as not to lose any data and to allow potential future cross-checking and investigation of any inconsistencies. This, combined with some long column names in the original spreadsheet, resulted in some long column names in the merged dataset. I kept these to ensure that all relevant details and labels were preserved in the merger. An alternative would be to create one or more new columns to contain this information.

The alphanumeric data in the "State" column was not consistent among the datasets. To remedy this, I removed all numerical characters, special characters (except periods), and trailing spaces from this column. The resulting columns are identical among the four sheets. I then used the merge tools in Python to combine the four data frames into one, joining them on the state column. The resulting dataset is output to a DataJoinSample.csv
