# hello-world
First Repository 
This readme file explains how what the py file works:

It includes the following:

- Dictionaries that was important to be seen by all functions that helps the translation of some values

* get_filters : 

-Asks user for input to choose the data accordingly, the user can choose all for months or days to get all the data
- output: city name , month name , day of the week name




* load_data :
- inputs: city name, month name, day of the week name
- it looks up the names in the dictionaries and assign it the write numbering to use as indices to look up data from the df with

- contains the method ( to_datetime) from pandas to make the datetime readable by pandas for future indexing
- ( infer_datetime_format= True) : I found this part online which is said to make the processing of the date faster than it would usually take

- it also ensures that the values taken by the user are in the dictionaries (this part is not well written but it works)

*get_key:
- this gets the key from a dictionary by giving it the value and the dictionary name

*raw_data:
- this function asks the user if they want to review the raw data by giving it a dataframe

THE REST OF THE FUNCTIONS are straight forward requiring nothing but the selected dataframe from all these functions
