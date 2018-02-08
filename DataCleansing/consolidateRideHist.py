
####      ####     ####      ####      ####
# USE CONSOLIDATEFILES.PY INSTEAD OF THIS #
####      ####     ####      ####      ####


#import csv
import os
import pandas as pd
import re
import time
# from unittest.mock import inplace

#stuff that is already accomplished in the other file
rootDir = r'c:/users/a3bw9zz/desktop/niceRideDownloads/'
unzipDir = r'c:/users/a3bw9zz/desktop/niceRideDownloads/unzipped/'
seasonFolder = os.listdir(unzipDir)[0]


for seasonFolder in os.listdir(unzipDir):
    #find the season dir
    seasonDir = unzipDir + seasonFolder
    #print(seasonDir)
    
    #find season history file
    file = [x for x in os.listdir(seasonDir) if re.match('^Nice_[Rr]ide_trip_history_20\d{2}_season.csv$', x)][0]
    print(file)
    #get season history
    seasonHist = pd.read_csv(seasonDir + '/' + file)
    
    # check the percent that are null
    print([k + ': ' + 
    str(round(sum(v.isnull()) / len(v), 3)) 
    for k, v in seasonHist.items()])

    # drop extra rows that have no data, id them based on having zero seconds for duration
    durCol = [x for x in seasonHist.columns if re.match('Total duration .*$', x)][0]
    #seasonHist = seasonHist[seasonHist[durCol] > 0]
    
    #convert durations to seconds
    if durCol == 'Total duration (ms)': 
        seasonHist[durCol] = seasonHist[durCol] / 1000
    
    """
    # figure out what all of the col names are to setup dict for standardizing the col names
    cols = []
    for seasonFolder in os.listdir(unzipDir):
        #find the season dir
        seasonDir = unzipDir + seasonFolder
        file = [x for x in os.listdir(seasonDir) if re.match('^Nice_[Rr]ide_trip_history_20\d{2}_season.csv$', x)][0]
        
        #get season history
        seasonHist = pd.read_csv(seasonDir + '/' + file)
        print(seasonHist.columns)
        
        #add col names
        cols = cols + list(seasonHist.columns)
    
    list(set(cols))
    """
    
    renameDict = {durCol: 'duration',
                  'Start terminal': 'sTerminal',
                  'Start station': 'sStation',
                  'Total duration (seconds)': 'duration',
                  'Total duration (ms)': 'duration',
                  'End station': 'eStation',
                  'Total duration (Seconds)': 'duration',
                  'Start date': 'start',
                  'Start station number': 'sTerminal',
                  'End date': 'end',
                  'End terminal': 'eTerminal',
                  'Account type': 'cust',
                  'End station number': 'eTerminal'}
    
    seasonHist.rename(columns=renameDict, inplace=True)
    
    seasonHist.rename(columns={'Start station number': 'sTerminal'}, inplace=True)
    
    #append to consolidated file
    try:
        seasonsdf = seasonsdf.append(seasonHist)        
    except NameError:
            seasonsdf = seasonHist.copy()
            print('initiated consolidated df from '+ re.match('.*\d{4}.*', file).group(0) + '\n')
    else:
        print('appended '+ re.match('.*\d.*', file).group(0) + ' to df \n')
    

# check the percent that are null
[k + ': ' + 
str(round(sum(v.isnull()) / len(v), 3)) 
for k, v in seasonsdf.items()]





"""
#get list of dirs with files to unzip
seasonFolders = [f[0] for f in os.walk(unzipDir)][1:]

seasonFolder = seasonFolders[0]

for seasonFolder in seasonFolders:
    #get ride history file
    files = [f[2] for f in os.walk(seasonFolder)][0]
    
    for zippedSeasonDir in files:
        print(zippedSeasonDir)
        
        
    file = [x for x in files if re.match('Nice_[Rr]ide_trip_history_20\d{2}_season.csv', x)]
    
    #read file
    pd.read_csv('c:/users/a3bw9zz/desktop/niceRideDownloads/Nice_ride_trip_history_2016_season.csv')
    pd.read_csv(unzipDir + file[0])
        


pd.read_csv()
"""
