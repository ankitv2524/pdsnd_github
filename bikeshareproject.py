### ******************************************** project work on " Explore US Bikeshare Data " ***************************************************************
import time
import datetime
import pandas as pd
import statistics as st

## Filenames
#chicago = 'chicago.csv'
#new_york_city = 'new_york_city.csv'
#washington = 'washington.csv'



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input('\nWould you like to see data for.?: Simply type the Name \n-> Chicago \n-> New York\n-> Washington\n').lower()
               #lower() is used to take input of any type formate

    while(True):
        if(city == 'chicago' or city == 'new york' or city == 'washington' or city == 'all of them'):
            break
        else:
            city = input('Sorry, I do not understand your input. Please input either '
                  'Chicago, New York, or Washington.\n(Enter Correct city):\t ').lower()
               #lower() is used to take input of any type formate
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('\nWhich month Data you want..?: Simply type the Name \n-> January \n-> February \n-> March \n-> April \n-> May \n-> June \n').lower()
               #.lower() is used to take input of any type formate
        
    while(True):
        if(month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all'):
            break
        else:
            month = input('\nPlease try to Enter valid month otherwise it will invalid and Not showing any result:\n').lower()
             #lower() is used to take input of any type formate   

            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day =  input('Which day Data you want..?  simply type the name \n-> Monday \n-> Tuesday  \n-> Wednesday  \n-> Thursday   \n-> Friday   \n-> Saturday  \n-> Sunday \n-> all to display data of all days\n').lower()
     #lower() is used to take input of any type formate  
    while(True):
        
        if(day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all'):
            break;
        else:
            day = input('\nPlease try to Enter valid Day otherwise it will invalid and Not showing any result:\nEnter Correct day:\t ').lower()
             #lower() is used to take input of any type formate  
                
    #return day

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
    df = pd.read_csv(CITY_DATA[city])

 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # to_datetime is used to convert(change) date into date format
    df['End Time'] = pd.to_datetime(df['End Time'])
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        #used to find index of month.
        month = months.index(month) + 1       

        df = df[df['Start Time'].dt.month == month]
        
    #filter data by day.
    if day != 'all': 
        df = df[df['Start Time'].dt.weekday_name == day.title()]
     #print 5 rows.
    print(df.head())
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most regular Times of Travelling\n Loading Please wait for a while  ........\n')
    start_time = time.time()

    # display the most common month
    if(month == 'all'):
        most_similar_month = df['Start Time'].dt.month.value_counts().idxmax()
        print('********************   Most common(popular) month is :'+ str(most_similar_month) + '        *********************')

    # display the most common day of week
    if(day == 'all'):
        most_similar_day = df['Start Time'].dt.weekday_name.value_counts().idxmax()
        print('********************   Most common(popular) day is : ' + str(most_similar_day) + '        *********************')

    # display the most common start hour
    most_similar_hour = df['Start Time'].dt.hour.value_counts().idxmax()
    print('********************   Most popular hour is : ' + str(most_similar_hour) + '        *********************')

    print("\n********************   This took %s seconds.        *********************" % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n********************   Calculating The Most Popular Stations and Trip...        *********************\n')
    start_time = time.time()

    # display most commonly used start station
    most_similar_start_station = st.mode(df['Start Station'])
    print('\n********************   Most common start station is {}        *********************\n'.format(most_similar_start_station))

    # display most commonly used end station
    most_similar_end_station = st.mode(df['End Station'])
    print('\n********************   Most common end station is {}        *********************\n'.format(most_similar_end_station))

    # display most frequent combination of start station and end station trip
    combination_trip = df['Start Station'].astype(str) + " to " + df['End Station'].astype(str)
    The_most_frequent_trip = combination_trip.value_counts().idxmax()
    print('\n********************   Most popular trip is from {}        *********************\n'.format(The_most_frequent_trip))

    print("\n********************   This took %s seconds.        *********************" % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n********************   Calculating Trip Duration...        *********************\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    time1 = total_travel_time
    day = time1 // (24 * 3600)
    time1 = time1 % (24 * 3600)
    hour = time1 // 3600
    time1 %= 3600
    minutes = time1 // 60
    time1 %= 60
    seconds = time1
    print('\n********************   Total travel time is {} days {} hours {} minutes {} seconds        *********************'.format(day, hour, minutes, seconds))


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    time2 = mean_travel_time
    day2 = time2 // (24 * 3600)
    time2 = time2 % (24 * 3600)
    hour2 = time2 // 3600
    time2 %= 3600
    minutes2 = time2 // 60
    time2 %= 60
    seconds2 = time2
    print('\n********************   Mean travel time is {} hours {} minutes {} seconds        *********************'.format(hour2, minutes2, seconds2))


    print("\n********************   This took %s seconds.        *********************" % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\n********************   Calculating User Stats...        *********************\n')
    start_time = time.time()

    # Display counts of user types
    no_of_subscribing_user = df['User Type'].str.count('Subscriber').sum()
    no_of_customers_using = df['User Type'].str.count('Customer').sum()
    print('\n********************   Number of subscribers are {}        *********************\n'.format(int(no_of_subscribing_user)))
    print('\n********************   Number of customers(users) are {}        *********************\n'.format(int(no_of_customers_using)))

    # Display counts of gender
    if('Gender' in df):
        count_male = df['Gender'].str.count('Male').sum()
        count_female = df['Gender'].str.count('Female').sum()
        print('\n********************   Number of male users are {}        *********************\n'.format(int(count_male)))
        print('\n********************   Number of female users are {}        *********************\n'.format(int(count_female)))


    # Display earliest, most recent, and most common year of birth
    if('Birth Year' in df):
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        most_similar_birth_year = st.mode(df['Birth Year'])
        print('\n Oldest Birth Year is: {}\n Youngest Birth Year is: {}\n Most popular Birth Year is: {}'.format(int(earliest_year), int(recent_year), int(most_similar_birth_year)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\n********************   Would you like to restart? Enter yes or no.        *********************\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()