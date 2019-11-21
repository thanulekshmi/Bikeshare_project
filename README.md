### Date created
November 18th,2019

### Title
Python Script to analyse US Bikeshare Data for Chicago, New York City and Washington:

### Description
This project was developed as a part of Data Analyst Nanodegree by Udacity. This python script is used to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. It computes the descriptive statistics for given data by importing the .csv files. It also takes the user's raw input and create an interactive experience in the terminal to present these statistics.

### Bike share Data

Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, data was provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

### The Datasets
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

### Statistics Computed

#1 Popular times of travel (i.e., occurs most often in the start time)
most common month
most common day of week
most common hour of day
#2 Popular stations and trip
most common start station
most common end station
most common trip from start to end (i.e., most frequent combination of start station and end station)
#3 Trip duration
total travel time
average travel time
#4 User info
counts of each user type
counts of each gender (only available for NYC and Chicago)
earliest, most recent, most common year of birth (only available for NYC and Chicago)

### Files used
chicago.csv
new_york_city.csv
washington.csv

### Required Libraries and Dependencies:
Python 3.x is required to run this project.

Additional required packages:
pandas
numpy


### Credits:
Lessons in the Introduction to Data Analysis section of Udacity's Data Analyst Nanodegree (DAND)
