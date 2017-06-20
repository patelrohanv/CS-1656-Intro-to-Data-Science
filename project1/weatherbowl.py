#!/usr/bin/python3
import argparse
import collections
import csv
import glob
import json
import math
import os
import pandas
import re
import requests
import string
import sys
import urllib
from calendar import monthrange as cal

def winner(t1, precip1, t2, precip2):
    win = '#'
    W = -1
    L = -1
    if precip1 > precip2:
        win = t1
        W = precip1
        L = precip2
    elif precip1 < precip2:
        win = t2
        W = precip2
        L = precip1
    elif precip1 == precip2:
        win =  "TIE"
    print("WINNER: " + win)
    percent = 100 * (float(W)/float(L) - 1)
    print("PERCENT: " + percent + "%")


#format weatherbowl.py team 1 team 2 year snow
#getting command line args
teamOne = sys.argv[1]
teamTwo = sys.argv[2]
year = sys.argv[3]
weather = sys.argv[4]

#if team does not contain snow, error
#lowercase teams
teamOne = teamOne.lower()
teamTwo = teamTwo.lower()

#declaring other arguements
teamOne_city = '#'
teamOne_airport = '#'
teamTwo_city = '#'
teamTwo_airport = '#'
printTeamOne = '#'
printTeamTwo = '#'

#opening and reading csv file
f = open('NFL_data.csv')
nflTeams = csv.reader(f)
for row in nflTeams:
    #print(row)
    club = row[0]
    city = row[1]
    airport = row[2]
    club = club.lower()
    city = city.lower()
    airport = airport.lower()
    if teamOne in club:
        teamOne = club
        printTeamOne = row[0]
        teamOne_city = city
        teamOne_airport = airport
    elif teamTwo in club:
        printTeamtwo = row[0]
        teamTwo = club
        teamTwo_city = city
        teamTwo_airport = airport

key = "56a0b6c761ac0272"
snow1 = 0
snow2 = 0

###
#ThIS ENTIRE CHUNK SHOULD BE IN A LOOP
#api.wunderground.com/api/<key>/history_<year><month><endofmonth>/q/<city>.json
###

#Requesting weather data JSONs
#api.wunderground.com/api/<key>/history_<year>0101/q/<city>.json
url_1 =  "http://api.wunderground.com/api/" + key + "/history_" + year + "0131/q/" + teamOne_airport + ".json"
url_2 = "http://api.wunderground.com/api/" + key +"/history_" + year + "0131/q/" + teamTwo_airport + ".json"
r1 = requests.get(url_1)
parsed_json1 = r1.json()
json1_snow = parsed_json1['history']['dailysummary'][0]['monthtodatesnowfalli']
if not json1_snow or json1_snow == 'T':
    json1_snow = 0
snow1 += float(json1_snow);
r2 = requests.get(url_2)
parsed_json2 = r2.json()
json2_snow = parsed_json2['history']['dailysummary'][0]['monthtodatesnowfalli']
if not json2_snow or json2_snow == 'T':
    json2_snow = 0
snow2 += float(json2_snow);

#Requesting weather data JSONs
#api.wunderground.com/api/<key>/history_<year>0101/q/<city>.json
url_1 =  "http://api.wunderground.com/api/" + key + "/history_" + year + "0228/q/" + teamOne_airport + ".json"
url_2 = "http://api.wunderground.com/api/" + key +"/history_" + year + "0228/q/" + teamTwo_airport + ".json"
lastday = cal(int(year), 2)
if(lastday == 29):
    url_1 =  "http://api.wunderground.com/api/" + key + "/history_" + year + "0229/q/" + teamOne_airport + ".json"
    url_2 = "http://api.wunderground.com/api/" + key +"/history_" + year + "0229/q/" + teamTwo_airport + ".json"
r1 = requests.get(url_1)
parsed_json1 = r1.json()
json1_snow = parsed_json1['history']['dailysummary'][0]['monthtodatesnowfalli']
if not json1_snow or json1_snow == 'T':
    json1_snow = 0
snow1 += float(json1_snow);
r2 = requests.get(url_2)
parsed_json2 = r2.json()
json2_snow = parsed_json2['history']['dailysummary'][0]['monthtodatesnowfalli']
if not json2_snow or json2_snow == 'T':
    json2_snow = 0
snow2 += float(json2_snow);

#Requesting weather data JSONs
#api.wunderground.com/api/<key>/history_<year>0101/q/<city>.json
url_1 =  "http://api.wunderground.com/api/" + key + "/history_" + year + "0331/q/" + teamOne_airport + ".json"
url_2 = "http://api.wunderground.com/api/" + key +"/history_" + year + "0331/q/" + teamTwo_airport + ".json"
r1 = requests.get(url_1)
parsed_json1 = r1.json()
json1_snow = parsed_json1['history']['dailysummary'][0]['monthtodatesnowfalli']
if not json1_snow or json1_snow == 'T':
    json1_snow = 0
snow1 += float(json1_snow);
r2 = requests.get(url_2)
parsed_json2 = r2.json()
json2_snow = parsed_json2['history']['dailysummary'][0]['monthtodatesnowfalli']
if not json2_snow or json2_snow == 'T':
    json2_snow = 0
snow2 += float(json2_snow);


#printing results
print("YEAR: " + year)
print("TYPE: SNOW" )
print("TEAM-1: " + printTeamOne)
print("CITY-1: " + teamOne_airport)
print("PRECIP-1: " + str(snow1))
print("TEAM-2: " + printTeamtwo)
print("CITY-2: " + teamTwo_airport)
print("PRECIP-2: " + str(snow2))

W = -1.0
L = -1.0

if snow1 > snow2:
    print("WINNER: " + printTeamOne)
    W = snow1
    L = snow2
elif snow1 < snow2:
    print("WINNER: " + printTeamtwo)
    W = snow2
    L = snow1
elif snow1 == snow2:
    print("WINNER: N0 WINNER")

if not snow1 or not snow2:
    print("PERCENT: infity%")
elif snow1 == 0 or snow2 == 0:
    print("PERCENT: infinity%")
else:
    W = float(W)
    L = float(L)
    percent = 100 * (W / L - 1)
    print('PERCENT: %.2f%%' %percent)
