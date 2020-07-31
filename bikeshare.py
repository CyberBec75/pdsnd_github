""" Created by Rebecca Roberts for Udacity Programming for Data Science Nanadegree"""
""" Date 31st July 2020"""

import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_LIST = ['january', 'february','march', 'april','may','june','all']

DAYS_LIST = ['monday','tuesday','wednesday', 'thursday', 'friday','saturday','sunday', 'all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!\n')
    print('You can exit this program any time by pressing Ctrl + c.')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ('chicago', 'new york city', 'washington')
    while True:
        city = input('\nWhich city would you like to see the statistics for?\n Please enter Chicago, New York City, or Washington\n').lower()
        if city not in cities:
            print('\Invalid entry. Please enter Chicago, New York City, or Washington\n')
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
    while True:
        month = input('\nWhich month would you like to filter by: January, February, March, April, May or June? If you do not want to filter by month, please enter "all"\n').lower()
        if month not in months:
            print('Invalid entry, please enter a valid month.')
            continue
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    while True:
        day = input('\nWhich day would you like to filter by: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? If you do not want to filter by day, please enter "all"\n').lower()
        if day not in days:
            print('Invalid entry, please try again.')
            continue
        else:
            break

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
    
    # record time taken to process this step
    start_time = time.time()
    
    print('Loading data and applyiong filters\n')
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime to create a start time column
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # convert the Start Time column to datetime to create an end time column
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month

    # extract day from the Start Time column to create a day of week column
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
          
    # filter by month if applicable and create new data fame
    if month != 'all':
    # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = MONTH_LIST.index(month) + 1 
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
    # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]     
        
    print("This calculation took %s seconds." % (time.time() - start_time))
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]
    print('The most common month is:', popular_month)

    # TO DO: display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print('The most common day is:', popular_day)

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common hour is:', popular_hour)


    print("\nThis calculation took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    Start_Station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is:', Start_Station)

    # TO DO: display most commonly used end station

    End_Station = df['End Station'].value_counts().idxmax()
    print('\nThe most commonly used end station is:', End_Station)

    # TO DO: display most frequent combination of start station and end station trip

    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nThe most commonly used combination of start station and end station trip is:', Start_Station, " & ", End_Station)

    print("\nThis calculation took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    Total_Travel_Time = sum(df['Trip Duration'])
    print('The total travel time in minutes is:', Total_Travel_Time/60, " Minutes")
   
    # TO DO: display mean travel time

    Mean_Travel_Time = df['Trip Duration'].mean()
    print('The mean travel time in minutes is:', Mean_Travel_Time/60, " Minutes")
   
    print("\nThis calculation took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].dropna()

    if user_type.empty:
        print('There is no user type data available for the filters you selected.')
    else:
        user_type = user_type.value_counts()
        print('The user type details are: {}'.format(user_type))

    # Display counts of gender
        if 'Gender' in df:
            user_gender = df['Gender'].dropna()
            if user_gender.empty:
                print('There is no user type data available for the filters you selected.')
            else:
                user_gender = user_gender.value_counts()
                print('The count of users by gender is: {}'.format(user_gender))

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        birth_years = df['Birth Year'].dropna()
        if birth_years.empty:
            print('There is no user type data available for the filters you selected.')
        else:
            user_birth_year = df['Birth Year'].dropna()
            if user_birth_year.empty:
                print('There is no user type data available for the filters you selected.')
            else:
                oldest_user = user_birth_year.min()
                print('The earliest year of user birth is: {}'.format(int(oldest_user)))

                youngest_user = user_birth_year.max()
                print('The most recent year of user birth is: {}'.format(int(youngest_user)))

                most_common_year_of_birth = user_birth_year.mode()[0]
                print('The most common birth year of users is: {}'.format(int(most_common_year_of_birth)))

    print("\nThis calculation took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def display_data(df):
    """Displays raw data."""
    choice = input('Would you like to look at the raw data? Please enter yes or no. ').lower()
    print()
    if choice=='yes':
        choice=True
    elif choice=='no':
        choice=False
    else:
        print('You did not enter a valid choice. Please enter yes or no. ')
        display_data(df)
        return

    if choice:
        while 1:
            for i in range(5):
                print(df.iloc[i])
                print()
            choice = input('Do you want to look at another five records? Please enter yes or no.').lower()
            if choice=='yes':
                continue
            elif choice=='no':
                break
            else:
                print('You did not enter a valid choice.Please enter yes or no.')
                return
   
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
