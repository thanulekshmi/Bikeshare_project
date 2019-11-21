
#Packages
import datetime
import calendar
import pandas as pd

#Dictionary

CITIES_DATA ={'chicago':'chicago.csv',
            'washington' : 'washington.csv',
            'new york city' : 'new_york_city.csv'}
MONTH_DATA = {'january': 1,
         'february': 2,
         'march' : 3,
         'april' : 4,
         'may' : 5,
         'june' : 6}
WEEK_DATA = {'monday' : 0,
             'tuesday': 1,
             'wednesday' : 2,
             'thursday' : 3,
             'friday' : 4,
             'saturday' : 5,
             'sunday' : 6}

#Methods

def get_city():
   """
   Asks the user to specify the city and returns the filename of the specified city
   Args : No argument
   Output: Returns the name of the file for the specified city
   """

   print("\nHello! Let\'s explore some US bikeshare data.")

   # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
   city=input("\nSelect a city ('Chicago', 'Washington','New York City') to see the data : ")
   city=city.lower()
   while True:
        if city in CITIES_DATA:
            filename=CITIES_DATA[city]
            break
        else:
            city=input("\nSelect a city ('Chicago', 'Washington','New York City') to see the data : ")
   return city,filename

def get_filters():
   """
        Asks the user to specify the time period and returns the appropiate filters
        Args : No argument
        Output: Returns the month and day filter
   """

   while True:
        # get user input to filter the data(month,day of the week or none)
        time_period = input("\nWould you like to filter the data by month and day of the week('month'), day of the week('day'), not at all ('none'): ").lower()

        # get user input for month (all, january, february, ... , june)
        if time_period=='month':
            while True:
                month=input("\nWhich month data would you like to analyze? Type the month name in full.").lower()
                if month not in MONTH_DATA:
                    print("\nPlease type the right option.")
                    continue
                else:
                    month=MONTH_DATA[month]
                    break
            while True:
              # get user input for day of week (all, monday, tuesday, ... sunday)
              filterByDayOfMonth = input("\nWould you like to filter by day of the week. Type 'y' or 'n':").lower()
              if filterByDayOfMonth=='y':
                   while True:
                        day=input("\nWhich day of the week would you like to analyze? Type the name of the day in full.").lower()
                        if day not in WEEK_DATA:
                           print("Please select the right options.")
                           continue
                        else:
                            day=WEEK_DATA[day]
                            return month,day
              elif filterByDayOfMonth=='n':
                    day='all'
                    return month,day
              else:
                    print("Please select the right options.")
        elif time_period == 'day':
            while True:
                # get user input for day of week (all, monday, tuesday, ... sunday)
                day=input("\nWhich day of the week would you like to analyze? Type the name of the day in full.").lower()
                if day not in WEEK_DATA:
                    print("Please select the right options.")
                    continue
                else:
                    day=WEEK_DATA[day]
                    month='all'
                    return month,day
        elif time_period == 'none':
            month='all'
            day='all'
            return month,day
        else:
            print ("Please choose the right options.")

def load_data(filename,month,day):
    """
        Load data for the specified filters of city(ies), month(s) and day(s) whenever applicable.
        Argument : Name of the city, month and day filter if applicable or "all" to apply no filter
        Output : panda dataframe containing city data filtered by month and day
    """
    # load data file into a dataframe
    df=pd.read_csv(filename)

    # convert the Start Time column to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month!='all':
        df=df[df['month']==month]

    # filter by day of week if applicable
    if day!='all':
       df=df[df['day_of_week']==day]

    return df

def time_stats(df):
    """
        Displays statistics on the most frequent times of travel.
        Argument : panda dataframe containing city data filtered by month and day
    """

    print('\nDisplaying statistics on most frequent times of travel:\n')

    # display the most common month
    most_common_month=df['month'].mode()[0]
    print("\n For the selected filter, the most favorite month to travel: " + calendar.month_name[most_common_month])

    # display the most common day of week
    most_common_day=df['day_of_week'].mode()[0]
    print("\n For the selected filter, the most favorite day of the week to travel: " + calendar.day_name[most_common_day])

    # display the most common start hour
    most_common_hour=df['hour'].mode()[0]
    print("\n For the selected filter, the most favorite hour of the week to travel: "+str(most_common_hour))

def station_stats(df):
    """
        Displays statistics on the most popular stations and trip.
        Argument : panda dataframe containing city data filtered by month and day
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')

    # display most commonly used start station
    most_common_start_station=df['Start Station'].mode()[0]
    print("\n For the selected filter, the most commonly used start station: "+most_common_start_station)

    # display most commonly used end station
    most_common_end_station=df['End Station'].mode()[0]
    print("\n For the selected filter, the most commonly used end station: "+most_common_end_station)

    # display most frequent combination of start station and end station trip
    df['Start - End']=df['Start Station']+' - '+df['End Station']
    most_common_start_end_station = df['Start - End'].mode()[0]
    print("\n For the selected filter, most frequent combination of start station and end station trip: "+most_common_start_end_station)

def trip_duration_stats(df):

    """
        Displays statistics on the total and average trip duration.
        Argument : panda dataframe containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration...\n')

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("\n Total time travelled :",total_travel_time)

    # display mean travel time
    avg_travel_time=df['Trip Duration'].mean()
    print("\n Average time travelled :",avg_travel_time)

def user_stats(df,city):
    """
        Displays statistics on bikeshare users.
        Argument : panda dataframe containing city data filtered by month and day

    """

    print('\nCalculating User Stats...\n')
    display()

    print("\nTotal count of different types of users :\n")
    # Display counts of user types
    user_counts=df['User Type'].value_counts()
    for index,user_count in enumerate(user_counts):
        print("{} : {}".format(user_counts.index[index],user_count))
    display()

    # Display counts of gender
    try:
        gender_counts=df['Gender'].value_counts()
        print("\nTotal count of each gender :\n")
        for index,gender_count in enumerate(gender_counts):
            print("{} : {}".format(gender_counts.index[index],gender_count))
        display()
    except KeyError:
        print("\n We are sorry! There is no data of user genders for the city "+ str(city)+"." )

    try:
    # Display earliest, most recent, and most common year of birth
        most_common_year_of_birth=int(df['Birth Year'].mode()[0])
        print("\n For the selected filter, the most common year of of birth amongst the riders: ",most_common_year_of_birth)

        earliest_year_of_birth=int(df['Birth Year'].min())
        print("\n For the selected filter, the oldest person to ride the bike: ",earliest_year_of_birth)

        youngest_year_of_birth=int(df['Birth Year'].max())
        print("\n For the selected filter, the youngest person to ride the bike: ",youngest_year_of_birth)

    except:
        print("\n We are sorry!There is no data of birth year for the city month"+ str(city)+".")



def display():
    """Prints 100 '-'"""
    print('-'*100)

def main():
    city,filename=get_city()
    display()

    month,day=get_filters()
    display()

    df=load_data(filename,month,day)
    print ("Data loaded. Computing the statics.....")
    display()

    time_stats(df)
    display()

    station_stats(df)
    display()

    trip_duration_stats(df)
    display()

    user_stats(df,city)
    display()

    # Restart?
    restart = input("\n * Would you like to restart and perform another analysis? Type \'yes\' or \'no\'.\n")
    if restart.upper() == 'YES' or restart.upper() == "Y":
        main()

#Main module

if __name__=="__main__":
    main()
