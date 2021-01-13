import time
import pandas as pd
import datetime as dt
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}




cities = []

for city, files in CITY_DATA.items():
    cities.append(city)

months = ["january", "february", "march", "april", "may", "june", "all"]

days = ["sunday", "monday", "tuesday", "wednesday", "thurday", "friday", "all"]

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please insert which city would like to filter: ")
        city = city.lower()
        if city in cities:
            print("Ok you have chosen city {} to filter by".format(city))
            break
        else:
            print("That city {},you have chosen is not available".format(city))
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter the month you want to filter by: ")
        month = month.lower()
        if month in months:
            print("You have chosen to filter by the month of {}".format(month))
            break
        else:
            print("Selected month {}, not available try again".format(month))
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("if you are looking for a certain day enter day here: ")
        day = day.lower()
        if day in days:
            print("you have decided to to filter day {}".format(day))
            break
        else:
            continue


    print('-'*40)

    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #Load csv file into dataframe using Pandas

    df = pd.read_csv(CITY_DATA[city])

    # as Start time is in string format use datetime to date time object

    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # Extract month and day from Start time to create new month and day columns

    df["month"] = df["Start Time"].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # if filtering by month need to convert month from string to int using index

    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month)+1

        # the above filtered month will create new dataframe

        df = df[df["month"] == month]

    # to filter by day of week if applicable to create new data frame

    if day != "all":

        df = df[df["day_of_week"] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month mode function for month with most values

    common_month = df["month"].mode()[0]
    print("Most common month", common_month)


    # TO DO: display the most common day of week

    common_day = df["day_of_week"].mode()[0]
    print("Most common  day of the week", common_day)


    # TO DO: display the most common start hour

    df["hour"] = df["Start Time"].dt.hour
    common_hour = df["hour"].mode()[0]
    print("Most common hour:", common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    print("The most popolar start is:", common_start_station)


    # TO DO: display most commonly used end station

    common_end_station = df["End Station"].mode()[0]
    print("The most common End Station is:", common_end_station)



    # TO DO: display most frequent combination of start station and end station trip

    df['combination'] = df['Start Station'] + " " + df['End Station']
    print("The most frequent combination of start station and end station trip is: ", df['combination'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df["Trip Duration"].sum()
    print("The total travel time is:", total_travel)


    # TO DO: display mean travel time

    averange_traveltime = df["Trip Duration"].mean()
    print("The averange travel time is:", averange_traveltime)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print(user_types, "\n")


    # TO DO: Display counts of gender

    if city != "washington":
        gender_counts = df["Gender"].value_count()
        print(gender_counts, "\n")

        earliest_birth = df["Birth Year"].min()
        most_recent_birth = df["Birth Year"].max()
        most_common_birth = df["Birth Year"].mode()[0]

     # TO DO: Display earliest, most recent, and most common year of birth
        print("Earliest birth is: ", earliest_birth)
        print("Most recent birth: ", most_recent_birth)
        print("Most common birth: ", most_common_birth)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def raw_data_load(df):
    """ This will display the raw data for filtered data"""

    i = 5

    while True:
        answer = input("Do you want to view raw data? Enter yes or no: ")
        answer = answer.lower()

        if answer == "yes":
            raw_data = df.head(i)
            print(raw_data)
            i += 5
            continue
        else:
            break

    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data_load(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
