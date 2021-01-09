import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
allowed_nyc = ['new york city', 'nyc', 'new york', 'ny']
allowed_chicago = ['chicago', 'chi']
allowed_washington = ['washington', 'dc','d.c', 'd.c.', 'washington dc', 'washington d.c', 'washington d.c.']
allowed_months = ['january', 'febuary', 'march', 'april', 'may', 'june', 'jan','feb','mar','apr','jun', '1', '01', '2', '02', '3', '03', '4', '04', '5', '05', '6', '06']
allowed_days = ['sunday', 'monday','tuesday','wednesday','thursday', 'friday', 'saturday', 'sun', 'mon', 'tue', 'wed', 'thur', 'fri', 'sat', '0', '1', '2', '3', '4', '5', '6']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('Select the city you would like to analyze: ').lower()
            if city in allowed_nyc:
                city = 'new york city'
                print('you have selected {}'.format(city))
                break
            elif city in allowed_chicago:
                city = 'chicago'
                print('you have selected {}'.format(city))
                break
            elif city in allowed_washington:
                city = 'washington'
                print('you have selected {}'.format(city))
                break
            else:
                print("Please only select from 'chicago', 'new york city', or 'washington'\n")

        except Exception as e:
            print(" Exception occurred: {}".format(e))
            print('\nEnter either: Chicago, New York City or Washington')

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month_filter = input('Would you like to filter by month? Answer [y/n]\n').lower()
            if (month_filter == 'n') or (month_filter =='no'):
                month = 'all'
                break
            elif (month_filter == 'y') or (month_filter =='yes'):
                month = input('Select the month you would like to analyze for:\n').lower()
                if True and (month in allowed_months):
                    if month == 'jan'or month == 'january' or month =='01' or month =='1':
                        month = 1
                        break
                    elif month == 'feb' or month == 'febuary' or month == '02' or month == '2':
                        month = 2
                        break
                    elif month == 'march' or month =='mar' or month =='3' or month =='03':
                        month = 3
                        break
                    elif month =='april' or month =='apr' or month =='4' or month =='04':
                        month = 4
                        break
                    elif month =='may' or month =='5' or month =='05':
                        month = 5
                        break
                    elif month == 'june' or month =='jun' or month =='6' or month =='06':
                        month = 6
                        break
                else:
                    print("\nOkay, lets try that again. \nPlease enter from the following months: january, febuary, march, april, may, june\n")
        except Exception as e:
                print(" Exception occurred: {}".format(e))
                print('\nEnter either: january, febuary, march, april, may, june')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day_filter = input('Would you like to filter by day? Answer [y/n]\n').lower()
            if (day_filter == 'n') or (day_filter =='no'):
                day = 'all'
                break
            elif (day_filter == 'y') or (day_filter == 'yes'):
                day = input('Enter the day of week you would like to filter by\nMonday = 0, Tuesday = 1, Wednesday = 2, Thursday = 3, Friday = 4, Saturday = 5, Sunday = 6\n').lower()
                if True and (day in allowed_days):
                    if (day == 'monday' or day == 'mon' or day == '0'):
                        day = 0
                        break
                    elif (day == 'tuesday' or day == 'tue' or day == 'tues' or day == '1'):
                        day = 1
                        break
                    elif (day == 'wednesday' or day == 'wed' or day == '2'):
                        day = 2
                        break
                    elif (day == 'thursday' or day == 'thu' or day == 'thur' or day == '3'):
                        day = 3
                        break
                    elif (day == 'friday' or day == 'fri' or day == '4'):
                        day = 4
                        break
                    elif (day == 'saturday' or day == 'sat' or day == '5'):
                        day = 5
                        break
                    elif (day == 'sunday' or day == 'sun' or day == '6'):
                        day = 6
                        break
                else:
                    print('\nOkay, lets try that again\nPlease enter the fullname of a valid weekday\n')
        except Exception as e:
            print(" Exception occurred: {}".format(e))
            print('Enter from the following: sunday, monday, tuesday, wednesday, thursday, friday, saturday ')

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

    #load the city into a DataFrame
    df = pd.read_csv(CITY_DATA[city])

    #convert the start_time into datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #create a month and weekday_name columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday

    #filter by month if applicable
    if month != 'all':
        df = df[df['month'] == month]

    #filter by day if applicable
    if day != 'all':
        df = df[df['day'] == day]

    print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    month_dict = {1: 'January', 2:'Febuary', 3:'March', 4:'April', 5:'May', 6:'June'}
    dow_dict = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # display the most common month
    mode_month = list(df['month'].mode())
    print('The most popular month(s) is/are: ', mode_month)

    # display the most common day of week
    mode_dow = list(df['day'].mode())
    print('The most common day of week is: ', mode_dow)

    # display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    mode_hour = list(df['Start Hour'].mode())
    print('The most common start hour is: ', mode_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    mode_start_station = df['Start Station'].mode()[0]
    print('The most common start station is: ', mode_start_station)

    # display most commonly used end station
    mode_end_station = df['End Station'].mode()[0]
    print('The most common end station is: ', mode_end_station)

    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'].astype(str) + ' TO ' + df['End Station'].astype(str)
    mode_trip= df['Trip'].mode()
    print('The most common trip is: ', mode_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel time is: ', total_travel_time, ' seconds')

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is: ', mean_travel_time, ' seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('User type count:\n', user_type_count)

    # Display counts of gender
    while True:
        try:
            if city != 'washington':
                gender_count = df['Gender'].value_counts()
                print('\nGender Count:\n', gender_count)
                break
            else:
                print('\nThere is no Gender data to analyze for Washington DC')
                break
        except Exception as e:
            break

    # Display earliest, most recent, and most common year of birth
    while True:
        try:
            if city!='washington':
                min_birth_year = int(df['Birth Year'].min())
                print('\nThe earliest Birth Year is: ', min_birth_year)

                max_birth_year = int(df['Birth Year'].max())
                print('The most recent Birth Year is: ', max_birth_year)

                mode_birth_year = list(df['Birth Year'].mode())
                print('The most common Birth Year is: ', mode_birth_year)
                break
            else:
                print('\nThere is no Birth Year data to analyze for Washington DC')
                break
        except Exception as e:
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    global city
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        start_row = 0
        end_row = 5
        while True:
            data = input('\nWould you like to display the raw data for the next 5 data points? [y/n]: ').lower()
            if data == 'yes' or data == 'y':
                pd.set_option('max_columns', None)
                pd.set_option('display.max_colwidth', -1)
                result = df.iloc[start_row: end_row]
                print(result)
                start_row = end_row
                end_row += 5
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
