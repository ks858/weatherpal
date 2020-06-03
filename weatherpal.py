import requests
import json
import pandas
import numpy
import matplotlib.pyplot as plt
from datetime import date

class LocationStats():

    def __init__(self,city):
        self.baseurl='http://api.weatherstack.com/forecast'
        self.city=city
        self.forecast_days=7
        self.units='f'
        self.hist_lower_bound=year_start = date(date.today().year, 1, 1)
        self.hist_upper_bound=year_end = date(date.today().year, 12, 31)
        self.apikey='6da06bcc2bc23480abb56e8882d83cdb'
        self.forecast=requests.get(self.baseurl, {'access_key': self.apikey,'query': city,'units':'f','forecast_days':self.forecast_days,'units':self.units}).json()

    def stats(self):
        requestdata=self.forecast['request']
        currentdata=self.forecast['current']
        forecastdata=self.forecast['forecast']
        forecastplot=pandas.DataFrame.from_dict(forecastdata,orient='index')[['date','avgtemp','mintemp','maxtemp']].to_string(index=False)
        '''
        Returns a stats summary of the current weather conditions for the requested locaton
        '''


        return '''
Current weather in {loc}:
Last updated time: {last_updated}

Current temperature: {temperature} (feels like {feelslike})

Weather forecast for the next 7 days:

{forecastplot}

Have a great week and enjoy the weather!

'''.format(
loc=requestdata['query'],
last_updated=currentdata['observation_time'],
temperature=currentdata['temperature'],
feelslike=currentdata['feelslike'],
forecastplot=forecastplot
)




usercity=input('\n\n\nEnter the name of a city for which you would like to see the weather forecast: ')
print('\n\n\n')
x=LocationStats(usercity)
print(x.stats())
