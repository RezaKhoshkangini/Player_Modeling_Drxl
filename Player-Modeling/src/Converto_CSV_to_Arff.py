'''
Created on Jun 12, 2017

@author: rezakhoshkangini
'''
import subprocess, os
import glob, os
from subprocess import call
from os import listdir
from os.path import isfile, join

def main():
    #listing the name of the csv files
    os.chdir("/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/Time_Based/Two/Binded_new")
    for filename in glob.glob("*.csv"):
        print(filename)
        # creating an empty ARFF file 
        file_out = open("/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/Time_Based/Two/Arff_new_binded"+str(filename)+'.arff', "w")
        call(['java', '-cp', '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Python_Code/weka.jar', 'weka.core.converters.CSVLoader', '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/Time_Based/Two/Binded_new/'+str(filename), '>', '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/Time_Based/Two/Arff_new_binded/'+str(filename)+'.arff'],
                        stdout=file_out)


if __name__ == '__main__':
    
    try:
        
        main()
    except Exception as ex:
        print(ex)

    print("Converting is Finished")