import glob
import os
from stat import ST_CTIME

# glob documentation: https://www.geeksforgeeks.org/how-to-use-glob-function-to-find-files-recursively-in-python/

# scan all subdirectories of the current directory for *.csv files  
for name in glob.glob("./**/*.csv", recursive=True):
    print(name)

list_of_files = glob.glob("./**/*.csv", recursive=True)

latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)

savedSet=set()
print('savedSet: ', savedSet)
mypath='./data'


nameSet=set()
for f in os.listdir(mypath):
    if f.endswith(".csv"):
        nameSet.add(f)
print('nameSet: ', nameSet)


newSet=nameSet-savedSet
print('newSet: ', newSet)


savedSet=newSet
print('savedSet: ', savedSet)