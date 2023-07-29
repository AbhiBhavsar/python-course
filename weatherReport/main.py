import csv
import pandas
# with open('weatherReport/weather-data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures =[]
#     for row in data:
#         if row[1]!='temp':
#             temperatures.append(int(row[1]))
#     print (temperatures[0:len(temperatures)])

data=pandas.read_csv('weatherReport/weather-data.csv')
# data_dict=data.to_dict()
# temp_list=data['temp'].to_list()
# avg_temp=sum(temp_list)/len(data_dict['day'])
print(data['temp'].max())