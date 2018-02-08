#import csv
import os
import pandas as pd
import re
# from unittest.mock import inplace

# os.chdir('c:/github/nicerideanalysis/')

#stuff that is already accomplished in the other file
rootDir = r'data/'
unzipDir = r'data/unzipped/'
seasonFolder = os.listdir(unzipDir)[0]
del seasonFolder

for seasonFolder in os.listdir(unzipDir):
    
    #find the season dir
    seasonDir = unzipDir + seasonFolder
    print(seasonDir)
    
    #find season history file
    file = [x for x in os.listdir(seasonDir) if re.match('^Nice_[Rr]ide_trip_history_20\d{2}_season.csv$', x)][0]
    print(file)
    #get season history
    seasonHist = pd.read_csv(seasonDir + '/' + file)
    
    #convert to lowercase names
    seasonHist.rename(columns={x: x.lower() for x in seasonHist.columns}, inplace = True)

    if 'start station number' in seasonHist.columns or 'end station number' in seasonHist.columns:
        seasonHist.rename(index=str, columns={'start station number': 'start terminal', 
                                              'end station number': 'end terminal'}, inplace = True)

    """    
    #make sure station number columns are actually strings
    stationNumCols = [x for x in seasonHist.columns if re.match('^.*number$', x)]

    for c in stationNumCols:
        seasonHist[c] = seasonHist[c].apply(str)
    """    
    
    # drop extra rows that have no data, id them based on having zero seconds for duration
    durCol = [x for x in seasonHist.columns if re.match('total duration .*$', x)][0]
    seasonHist = seasonHist[seasonHist[durCol] > 0]
    
    #convert durations to seconds
    if durCol == 'total duration (ms)': 
        seasonHist[durCol] = seasonHist[durCol] / 1000
        seasonHist.rename(columns={durCol: 'total duration (seconds)'}, inplace=True)

    #find season locations file    
    file = [x for x in os.listdir(seasonDir) if re.match('^Nice_Ride_20\d{2}[_-][Ss]tation[_-][Ll]ocations ?.csv$', x)][0]
    print(file)
    #get season locations
    seasonLocs = pd.read_csv(seasonDir + '/' + file)
    
    #convert to lowercase names
    seasonLocs.rename(columns={x: x.lower() for x in seasonLocs.columns}, inplace = True)
    
    # drop unnamed columns
    dropCols = [x for x in seasonLocs.columns if re.match('unnamed|notes', x)]
    
    if len(dropCols) > 0:
        seasonLocs.drop(dropCols, axis = 1, inplace=True)
    
    if 'name' in seasonLocs.columns:
        seasonLocs.rename(index=str, columns={'name': 'station'}, inplace = True)

    if 'longitude' in seasonLocs.columns:
        seasonLocs.rename(index=str, columns={'longitude': 'long'}, inplace = True)
        
    if 'latitude' in seasonLocs.columns:
        seasonLocs.rename(index=str, columns={'latitude': 'lat'}, inplace = True)

    if 'nbdocks' in seasonLocs.columns:
        seasonLocs.rename(index=str, columns={'nbdocks': 'nb docks'}, inplace = True)
        
    if 'total docks' in seasonLocs.columns:
        seasonLocs.rename(index=str, columns={'total docks': 'nb docks'}, inplace = True)
        
    if 'number' in seasonLocs.columns:
        seasonLocs.rename(index=str, columns={'number': 'terminal'}, inplace = True)



    """    
    #make sure station number columns are actually strings
    stationNumCols = [x for x in seasonHist.columns if re.match('^.*number$', x)]

    for c in stationNumCols:
        seasonHist[c] = seasonHist[c].apply(str)
    """
    
    #join the history and locations
    
        #join on the start location
        #change names of loc columns, since we are using locs twice (start and end of ride)
        
    leftCol = [x for x in seasonHist.columns if re.match('^start station$', x)][0]
    seasondf = pd.merge(seasonHist, seasonLocs.rename(index=str, columns={k:'s_'+k for k in seasonLocs.columns}), 
                        how='left', left_on = leftCol, right_on = 's_station')

    
    seasondf.head(3)

        #join on the end location
        #also change names to add prefix
    leftCol = [x for x in seasonHist.columns if re.match('^end station$', x)][0]
    seasondf = pd.merge(seasondf, seasonLocs.rename(str, columns={k:'e_'+k for k in seasonLocs.columns}), 
                        how='left', left_on = leftCol, right_on = 'e_station')
    seasondf.head(3)

    # warn new columns
    if file != 'Nice_Ride_2010_station_locations.csv':
        for c in seasondf.columns:
            if c not in seasonsdf.columns:
                print('Introducing Column: '+ c)
        
    #append to consolidated file
    try:
        seasonsdf = seasonsdf.append(seasondf)        
    except NameError:
            seasonsdf = seasondf.copy()
            print('initiated consolidated df from '+ re.match('.*\d{4}.*', file).group(0))
    else:
        print('appended '+ re.match('.*\d.*', file).group(0) + ' to df')
    
    print('\n')
    
    if seasonsdf.shape[1] > 22:
        break






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

