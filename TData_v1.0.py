# TData_v1.0
# Python 3 code to generate test Data project files
# No input arguments required
# System looks to see where it is running from  
# Config.txt file is assumed to be in the root directory along with the source code  
# Data files placed in directory \data - this is platform independent
# Write to a log file as well to screen
#
# b.brooks 05/2020

import os
from os import path
from datetime import datetime
import TData_parser as td


# change working directory to the directory where the code is being run from 
try:
    os.chdir(os.path.dirname(__file__))
    print("Current Working directory: ", os.getcwd())
except:
    print("Already in correct directory") 

# create log file new one per day
today = datetime.utcnow().strftime('%Y-%m-%d')
logfile = os.path.join(today + '.log')
g = open(logfile, 'a')
g.close()

# check for Data directory
try:
    dirName = 'Data'
    os.mkdir(dirName)
    print("Directory " , dirName ,  " created ") 
    g = open(logfile, 'a')
    g.write(datetime.utcnow().isoformat() + ' Data directory created.\n')
    g.close()
except FileExistsError:
    print("Directory " , dirName ,  " already exists")
    g = open(logfile, 'a')
    g.write(datetime.utcnow().isoformat() + ' Data directory already exists.\n')
    g.close()
   
# check for config file
try:
    path.exists("config.txt")
    print("Config.txt file detected")
    g = open(logfile, 'a')
    g.write(datetime.utcnow().isoformat() + ' Config.txt file detected.\n')
    g.close()    
except FileExistsError:
    print("Config.txt file missing. Program will terminate.")
    g = open(logfile, 'a')
    g.write(datetime.utcnow().isoformat() + 'Config.txt file missing. Program terminated.\n')
    g.close()
    exit()
    
# check for lookup file - list of instruments and what data products are associated with them
try:
    path.exists("lookup.xlsx")
    print("lookup.xlsx file detected") 
    g = open(logfile, 'a')
    g.write(datetime.utcnow().isoformat() + ' lookup.xlsx file detected.\n')
    g.close()     
except FileExistsError:
    print("lookup.xlsx file missing. Program will terminate.")
    g = open(logfile, 'a')
    g.write(datetime.utcnow().isoformat() + ' lookup.xlsx file missing. Program wil terminate.\n')
    g.close() 
    exit()   
    
# check for meta
try:
    path.exists("meta_1.1.xlsx")
    print("meta_1.1.xlsx file detected")  
    
    path.exists("meta_2.0.xlsx")
    print("meta_2.0.xlsx file detected")
    
    g = open(logfile, 'a')
    g.write(datetime.utcnow().isoformat() + ' meta_1.1.xlsx file detected.\n')
    g.write(datetime.utcnow().isoformat() + ' meta_2.0.xlsx file detected.\n')
    g.close()     
except FileExistsError:
    print("meta.xlsx file missing. Program will terminate.")
    g = open(logfile, 'a')
    g.write(datetime.utcnow().isoformat() + ' meta.xlsx file missing. Program will terminate.\n')
    g.close() 
    exit()
    
td.t_control(logfile)    