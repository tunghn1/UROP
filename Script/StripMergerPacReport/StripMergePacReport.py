'''
Created on Apr 10, 2019

@author: TungNguyen230893
'''

import os
import glob
import csv

# Change directory and get all file name
outputFile = "E:/Project/UROP/PacReport.csv" 

os.chdir("E:/Project/UROP/PAC")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
fileNumber = 1   
csvColumns  = [' cfg_file', ' cyclomatic_complexity', ' npath_complexity', ' path_cplxty_class', ' path_cplxty_asym', ' path_cplxty']
try: 
    with open (outputFile, 'w+') as mergeFile:
        for file in all_filenames:
            with open (file, 'r') as inputFile:
                if (fileNumber == 1):
                    fileContent = csv.DictReader(inputFile)
                    fileHeader  = fileContent.fieldnames
                    
                    # Fix blank space after every data
                    writer      = csv.DictWriter(mergeFile, delimiter=',', lineterminator='\n', fieldnames=csvColumns)
                    writer.writeheader()
                    
                    for row in fileContent:
                        if (row[fileHeader[0]] in (None, "") or
                            row[fileHeader[1]] in (None, "") or
                            row[fileHeader[2]] in (None, "") or
                            row[fileHeader[3]] in (None, "")):
                            continue
                        else:
                            writer.writerow({fileHeader[1]:row[fileHeader[1]],
                                            fileHeader[2]:row[fileHeader[2]],
                                            fileHeader[3]:row[fileHeader[3]],
                                            fileHeader[4]:row[fileHeader[4]],
                                            fileHeader[5]:row[fileHeader[5]],
                                            fileHeader[6]:row[fileHeader[6]]})
                    ++fileNumber       
                else:   
                    fileContent         = csv.DictReader(inputFile)
                    fileHeader          = fileContent.fieldnames
                    a_line_after_header = next(fileContent)
                    
                    # Fix blank space after every data
                    writer              = csv.DictWriter(mergeFile, delimiter=',', lineterminator='\n', fieldnames=csvColumns)
                    
                    for row in fileContent:
                        if (row[fileHeader[0]] in (None, "") or
                            row[fileHeader[1]] in (None, "") or
                            row[fileHeader[2]] in (None, "") or
                            row[fileHeader[3]] in (None, "")):
                            continue
                        else:
                            writer.writerow({fileHeader[1]:row[fileHeader[1]],
                                            fileHeader[2]:row[fileHeader[2]],
                                            fileHeader[3]:row[fileHeader[3]],
                                            fileHeader[4]:row[fileHeader[4]],
                                            fileHeader[5]:row[fileHeader[5]],
                                            fileHeader[6]:row[fileHeader[6]]})
                    ++fileNumber
except IOError:
    print("I/O error")                   