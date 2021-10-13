# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 10:35:08 2021

@author: ajax2
"""
import time
import pandas as pd
from datetime import datetime,timedelta


CITY_DATA = { 'chicago': 'chicago.csv','new york city': 'new_york_city.csv', 'washington': 'washington.csv' }
months1={'january':1, 'february':2, 'march':3,'april':4,'may':5, 'june':6,'all':0}
weekdays={'sunday':6, 'monday':0, 'tuesday': 1, 'wednesday':2, 'thursday':3,'friday':4,'saturday':5, 'all':8}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    while True:
            print("Please Choose 'Chicago, New York or Washington to view their Data: '" )
        
            x=input().lower()
            try:
                if x=='chicago':
                    city='chicago'
                elif x=='new york':
                    city='new york city'
                elif x=='washington':
                    city= 'washington'
                print('You have Selected: ' ,city.title())
                break;
            except:
       
                    print("Please enter a valid choice!")
            
            continue
    while True:   
            print('The Data available is for the first 6 months of the year, Choose a month from January to June or type in "all" to inspect all the data:')
            y=input().lower()
            
            month1=" "

                
            if y.lower() in months1.keys():
                
                month1=months1[y]
                
                print('You have Selected: ', y.title())
                break
            elif y=='all':
                month1=0
                print('You have Selected: ', y.title())
                break
            else:
                print("Please enter a valid choice!")
            continue
            
    while True:   
            print('Please type the name of the weekday you want to inpsect, or type in "all" to inspect all days of the week:')
            z=input().lower()
            
            
           
            if str(z) in weekdays.keys():
                day1=weekdays[z.lower()]
                print('You have Selected: ', z.title())
                break
            elif y=='all':
                day1=0

                print('You have Selected: ', z.title())
                break
            else:
                print("Please enter a valid choice!")
                    
    return city,month1,day1
       
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)
    
def load_data(city,month1,day1):
    # Reading the File and Loading the DF
        city=str(city)
        filename=pd.read_csv(CITY_DATA[city])
        df=pd.DataFrame(filename)
        
        #Editing the unnamed Column as ID
        df.rename(columns = {'Unnamed: 0':'ID'}, inplace = True)
        
        #Converting the datetime to a readable format by Pandas
        
        df['Start Time'] = pd.to_datetime(df['Start Time'], format="%Y-%m-%d %H:%M:%S", infer_datetime_format=True)
        df['End Time'] = pd.to_datetime(df['End Time'], format="%Y-%m-%d %H:%M:%S", infer_datetime_format=True)
        
        #Ensuring the right input is taken
        
        if month1 in range(1,7):
            df=df[df['Start Time'].dt.month == month1]
        elif month1 == 0:
            df=df
        if day1 in range(0,7):
            df=df[df['Start Time'].dt.dayofweek==day1]
        elif day1==8:
            df=df
   
        return df


    
def get_key(val,dict1):
    # A function that returns the key of a value from a dictionary by taking the value and the dictionary
    for key, value in dict1.items():
         if val == value:
            return key 
def raw_data(df):
    # A function that asks if the user wants to look at the first 5 lines of the raw data
    i=0
    while True:
        if i==0:
            print('Would you like to see the first 5 rows of raw data? Type Yes or No')
        else:
            print('Would you like to see the  5 more lines of raw data? Type Yes or No')
        
        x=input().lower()
        if x=='yes':
            print(df.iloc[i:i+5,:])
            i+=5
        elif x=='no':
            break
def converter(x):
    n_day=x//86400
    n_hour=(x %86400)//3600
    n_min=((x %86400)%3600)//60
    n_sec=((x %86400)%3600)%60
    return n_day,n_hour,n_min,n_sec        
        
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    
    mcm=df['Start Time'].dt.month.value_counts().idxmax()   
    print('The Most Common Month is : ', get_key(mcm,months1).title())

    
    # display the most common day of week
    
    dow=df['Start Time'].dt.dayofweek.value_counts().idxmax()
    print('The Most Common Day of Week is :', get_key(dow,weekdays).title())

        
    # display the most common start hour
    
    SH=df['Start Time'].dt.hour.value_counts().idxmax()
    print('The Most Common Start Hour is:', SH)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    SS=df['Start Station'].value_counts().idxmax()
    print('The Most Commonly Used Start Station is : {}  With the Count Of: {}'.format( SS, df['Start Station'].value_counts().max()))

    # display most commonly used end station
    ES=df['End Station'].value_counts().idxmax()
    print('The Most Commonly Used End Station is : {}  With the Count Of: {}'.format( ES, df['End Station'].value_counts().max()))

    # display most frequent combination of start station and end station trip
    
    SE=df.groupby(['Start Station'])['End Station'].value_counts().idxmax()
    print('The Most Frequent Combination of Start and End Stations is: {} with the count of: {}'.format( SE,df.groupby(['Start Station'])['End Station'].value_counts().max()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    TTTs=int(df['Trip Duration'].sum())
    print('The Total Travel Time for All Users is: {} Seconds'.format(TTTs))
    d,h,m,s=converter(TTTs)
    
    print('Or:{} day(s) {} hour(s) {} minutes and {} seconds'.format(d,h,m,s))

    # display mean travel time
    MTT=int(df['Trip Duration'].mean())
    print('The Mean Travel Time for All Users is:',MTT)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User types: \n',df['User Type'].value_counts())

    # Display counts of gender
    if 'Gender'in df.columns:
        print('The Genders of the Users are: \n',df['Gender'].value_counts())
        
    else:
        print('Gender data is not available for this City')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('The Earliest Birth Year is: ',df['Birth Year'].min())
        print('The Most Recent Birth Year is: ',df['Birth Year'].max())
        print('The Most Common Birth Year is: ',df['Birth Year'].mode())
        print("\nThis took %s seconds." % (time.time() - start_time))
    else:
        print('Birth Data is not Available for this City')
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
