import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = input("Please enter city - Chicago, New York City, Washington.\n")
    while city.lower() not in ['chicago', 'new york city', 'washington']:
        city = input("Please enter chicago, new york city, washington.\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please enter month - all, january, february, ... , june\n")
    while month.lower() not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        month = input("Please enter month - all, january, february, ... , june\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please enter day of week - all, monday, tuesday, ... sunday\n")
    while day.lower() not in ('all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'):
        day = input("Please enter day of week - all, monday, tuesday, ... sunday\n")

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

    if city == 'new york city':
        city = 'new_york_city'

    #Load csv file
    df = pd.read_csv(city + ".csv")

    # convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':

        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    #Print time title
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()
    print("Most common month: ",common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].value_counts().idxmax()
    print("Most common day: ", common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("Most common hour: ", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print("Most common start station: ", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print("Most common end station: ", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    comb_station = df['Start Station'] + " to " +  df['End Station']
    common_station = comb_station.mode()[0]
    print("Most common station: ", common_station)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time: ", total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time: ", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):

    x = -5

    while (input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n').lower() != 'no'):
        print(df[x:x+5])
        x += 5

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Total user types: \n' + str(user_types))

    try:
        # TO DO: Display counts of gender
        gender_types = df['Gender'].value_counts()
        print('Total gender types: \n' + str(gender_types))
    except:
        print('No gender data for Washington')

    try:
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        latest = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print('Earlist: ' + str(earliest))
        print('Latest: ' + str(latest))
        print('Most common: ' + str(most_common))
    except:
        print('No Birth Year data for Washington')

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

	#Ask user if they want to restart
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
