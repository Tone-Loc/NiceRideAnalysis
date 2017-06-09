#import csv
import os
import urllib.request

def createDir(dir):
    #create storage directory
    if not os.path.exists(dir):
        os.mkdir(dir)


def setupDir(dir, dirType, returnDir=False):
    #make sure a string was provided and one of the dir types allowed
    if not isinstance(dir, str): 
        raise TypeError('Requires two string args, dir not a string')
    elif not isinstance(dirType, str): 
        raise TypeError('Requires two string args, dirType not a string')
    elif dirType not in ('root','zipped','unzipped'):
        raise TypeError("'Requires dirType of 'root','zipped' or 'unzipped'")
    
    #define the name of the new dir
    if dirType == 'root':
        if dir.endswith('/'): newDir = dir
        else: newDir = dir + '/'
    elif dirType == 'zipped':
        newDir = dir + 'zipped/'
    elif dirType == 'unzipped':
        newDir = dir + 'unzipped/'
    
    #create the new dir
    createDir(newDir)
    
    #return address of newDir
    if returnDir: return newDir

def unzipAll(zipDir, unzipDir):
    import zipfile
    
    #get list of files in zipDir
    zipFiles = os.listdir(zipDir)
    
    #unzip files in zipDir
    for f in zipFiles:
        fullFileAddress = zipDir + f
        zip_ref = zipfile.ZipFile(fullFileAddress, 'r')
        zip_ref.extractall(unzipDir)
        zip_ref.close()

def main():
    #define main storage directory
    rootDir = r'c:/users/a3bw9zz/desktop/niceRideDownloads/'
    
    #create root storage directory
    setupDir(rootDir, 'root')
     
    #create download storage dir
    zipDir = setupDir(rootDir, 'zipped', True)

    #establish set of web addresses where the data is hosted
    csvWebAddresses = dict(y2010 = 'https://niceridemn.egnyte.com/dd/byJLtGzvHM', 
                           y2011 = 'https://niceridemn.egnyte.com/dd/8xAYjDuS3L',
                           y2012 = 'https://niceridemn.egnyte.com/dd/GlYmbU2Bh0',
                           y2013 = 'https://niceridemn.egnyte.com/dd/kdJ4WP0mHC',
                           y2014 = 'https://niceridemn.egnyte.com/dd/MZxvOEELWQ',
                           y2015 = 'https://niceridemn.egnyte.com/dd/9nSKfEfxQ8',
                           y2016 = 'https://niceridemn.egnyte.com/dd/gYLZtGrwEk')
    
    #download the data
    for y in csvWebAddresses.keys():     
        urllib.request.urlretrieve(csvWebAddresses[y], zipDir + y + '.zip')

    #

    #create dir to unzip files to
    unzipDir = setupDir(rootDir, 'unzipped', True)
    
    #unzip the files
    unzipAll(zipDir, unzipDir)

if __name__ == "__main__": main()
