# Date created

The project was created on the 2nd January 2021

# Bike share Data exploration for Chicago, New York City and Washington


# Description

In this project, i made use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. I wrote code to import the data and answer interesting questions about it by computing descriptive statistics. i wrote a script that takes in raw input to create an interactive experience in the terminal or code editors to present these statistics.
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

# link to CSV Data and Data Set

https://www.divvybikes.com/system-data

The Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

Start Time (e.g., 2017-01-01 00:07:57)
End Time (e.g., 2017-01-01 00:20:53)
Trip Duration (in seconds - e.g., 776)
Start Station (e.g., Broadway & Barry Ave)
End Station (e.g., Sedgwick St & North Ave)
User Type (Subscriber or Customer)
The Chicago and New York City files also have the following two columns:

Gender
Birth Year


#Statistics Computed

1 Popular times of travel (i.e., occurs most often in the start time)

most common month
most common day of week
most common hour of day

2 Popular stations and trip

most common start station
most common end station
most common trip from start to end (i.e., most frequent combination of start station and end station)

3 Trip duration

total travel time
average travel time

4 User info

counts of each user type
counts of each gender (only available for NYC and Chicago)
earliest, most recent, most common year of birth (only available for NYC and Chicago)


The original files are much bigger but they can be accessed here if you'd like to see them (Chicago, New York City, Washington). These files had more columns and they differed in format in many cases. Some data wrangling has been performed to condense these files to the above core six columns to make analysis and the evaluation by Python more straightforward.

# Files and Code editors used

You should have Python 3, NumPy, and pandas installed
A text editor, like Sublime or Atom.
A terminal application (Terminal on Mac and Linux or Cygwin on Windows)
Git
Github
chicago.csv
new_york_city.csv
washington.csv


# Credits

https://stackoverflow.com/questions/59494111/pandas-python-value-counts-or-idxmax-returns-different-value-each-time

https://stackoverflow.com/questions/60214194/error-in-reading-stock-data-datetimeproperties-object-has-no-attribute-week

https://www.geeksforgeeks.org/python

https://www.tutorialspoint.com/python/python_classes_objects.htm

https://docs.python.org/3/library/stdtypes.html#functions

https://www.w3schools.com/python/pandas_tutorial.asp

udacity.com/project

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html

https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
