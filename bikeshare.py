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
    
    #while loop for error checking user input
    while True:
            #get user input for city (chicago, new york city, washington). 
            city = input("\nWhich city do you want to see the data for chicago, new york city, or washington:\n")
            city = city.lower()
            inputcity = ['chicago' ,'new york city', 'washington']
            if(city in inputcity):
              break
                  
            else:
              print("Not a valid city please try again")
              continue
       
    #while loop for error checking user input for filtering method
    while True:
          #get user input for method of filtering month, day, or no filter
          filter = input("\nDo you want to filter by month, day, or no filter please type no for no filter:\n")
          filter = filter.lower()
          
          if(filter == 'month' or filter == 'day' or filter == 'no'):
            break
          
          else:
            print("Not a valid filtering method please try again")
            continue

    #while loop for checking error for month and day filters
    while True: 
        #get user input for month (january, february, ... , june) if month is chosen
        if filter == 'month':
          month = input("\nwhich month do you want to filter by january, february, march, april, may, or june:\n")
          month = month.lower()
            inputmonth = ['january' ,'february' ,'march' ,'april' , 'may' ,'june']
          day = 'all'
            
          if(month in inputmonth):
            break
              
          else:
            print("Not a valid month try again:")
            continue
              
       #get user input for day of week (all, monday, tuesday, ... sunday) if day is chosen 
        if filter == 'day':
          day = input("\nwhich day do you want to filter by monday, tuesday, wednesday, thursday, friday, saturday, or sunday:\n")
          day = day.lower()
          month = 'all'
          inputday = ['monday' , 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'saturday' , 'sunday']
          if(day in inputday):
            break
            
          else:
            print("Not a valid day try again:")
            continue
            
        #if no filter is selected set both month and day to all
        if filter == 'no':
            month = 'all'
            day = 'all'
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
        
        using udacity practice problem 3
    """
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

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

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month
    print("The most common month in selected data is:\n", df['month'].mode(),"\n")

    #display the most common day of week
    print("The most common day of the week in selected data is:\n", df['day_of_week'].mode(),"\n")

    #display the most common start hour
    print("The most common start hour in selected data is:\n", df['Start Time'].dt.hour.mode(),"\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    print("The most commonly used start staion in selected data is:\n", df['Start Station'].mode(),"\n")

    #isplay most commonly used end station
    print("The most commonly used end staion in selected data is:\n", df['End Station'].mode(),"\n")


    #most frequent combination of start station and end station trip
    print("most frequent combination of start station and end station trip in selected data is:\n", (df['Start Station'] + ' and ' + df['End Station']).mode(),"\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
    print("The total travel time in selected data is:\n", df['Trip Duration'].sum(),"\n")

    # display mean travel time
    print("The mean travel time in selected data is:\n", df['Trip Duration'].mean(),"\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    print("The counts of user types in selected data is:\n", df['User Type'].value_counts(),"\n")

    #Display counts of gender if city is not Washington
    if city != 'washington':
        print("The counts of gender in selected data is:\n", df['Gender'].value_counts(),"\n")
    else:
        print("No gender data available")

    #Display earliest, most recent, and most common year of birth if city is not Washington
    if city != 'washington':
        print("The earliest year of birth in selected data is:\n", df['Birth Year'].min(),"\n")
        print("The most recent year of birth in selected data is:\n", df['Birth Year'].max(),"\n")
        print("The most common year of birth year of birth in selected data is:\n", df['Birth Year'].mode(),"\n")
    else:
        print("No year of birth data available")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        
        answer = input("\nWould you like to see the data? Enter any key for yes and type no for no.\n")
        answer = answer.lower()
        current_row = 5

         
        while answer != 'no':    
            print(df.head(current_row))
            answer = input("\nWould you like to see the next 5 rows of the data? Enter yes or no.\n")
            answer = answer.lower()
            current_row += 5
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
