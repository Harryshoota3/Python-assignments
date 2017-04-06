'''
Now You Code 4: Syracuse Weather

Write a program to load the Syracuse weather data from Dec 2015 in
JSON format into a Python list of dictionary. The file is:

"NYC4-syr-weather-dec-2015.json"

After you load this data calculate the number of days where the
'Mean TemperatureF' is above freezing ( > 32 degrees)

Store the days above freezing and below freezing into a dictionary
and then print out the dictionary like this:

{'below-freezing': 4, 'above-freezing': 27}

'''

# TODO: Write Todo list then beneath write your code


# Write code here

import json

with open('NYC4-syr-weather-dec-2015-this-week.json') as json_data:
    daily_temp = json.load(json_data)

cold_day = 0
hot_day = 0

for day in daily_temp:
    for temp in day:
        if(isinstance(day[temp],int) or isinstance(day[temp],float)):
           if day[temp] > 32:
               hot_day = hot_day + 1

           elif day[temp] < 32:
               cold_day = cold_day + 1
        
temp_stats = {}
temp_stats["below-freezing"] = cold_day
temp_stats["above-freezing"] = hot_day
print(temp_stats)
