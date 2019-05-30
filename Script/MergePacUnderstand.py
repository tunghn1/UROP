'''
Created on Mar 11, 2019

@author: TungNguyen230893
'''
from collections import defaultdict
import csv

# define path variable for understand, pac, and merge csv files to read, read, and write operation accordingly
UnderstandPath      = "C:/Users/TungNguyen230893/Desktop/UCI/Winter2019/Inf199/new_time_buggy_db.csv"
PacPath             = "C:/Users/TungNguyen230893/Desktop/UCI/Winter2019/Inf199/complexityOutput/new_time_17_buggy_classes.csv"
MergePath           = "C:/Users/TungNguyen230893/Desktop/UCI/Winter2019/Inf199/merge_pac_understand.csv"

# define dictionary
# UnderstandDict    = defaultdict(lambda: 0)

try:
    with open(UnderstandPath, 'r') as UnderstandFile, open(PacPath, 'r') as PacFile, open(MergePath, 'w+') as MergeFile:

        MergeHeader         = []
        Row                 = []
        UnderstandContent   = csv.DictReader(UnderstandFile)
        UnderstandHeader    = UnderstandContent.fieldnames
        PacContent          = csv.DictReader(PacFile)
        PacHeader           = PacContent.fieldnames
        MergeHeader.extend(PacHeader)
        MergeHeader.extend(UnderstandHeader)
        
        writer              = csv.DictWriter(MergeFile, fieldnames=MergeHeader)
        writer.writeheader()
        
           
        for PacRow in PacContent:     
            for UnderstandRow in UnderstandContent:
                PacNameFile = PacRow[PacHeader[1]].strip()
                UnderstandNameFile = UnderstandRow[UnderstandHeader[1]].strip()
                if (PacNameFile == UnderstandNameFile):
                    writer.writerow({PacHeader[0]:PacRow[PacHeader[0]],
                                     PacHeader[1]:PacRow[PacHeader[1]],
                                     PacHeader[2]:PacRow[PacHeader[2]],
                                     PacHeader[3]:PacRow[PacHeader[3]],
                                     PacHeader[4]:PacRow[PacHeader[4]],
                                     PacHeader[5]:PacRow[PacHeader[5]],
                                     PacHeader[6]:PacRow[PacHeader[6]],
                                     UnderstandHeader[0]: UnderstandRow[UnderstandHeader[0]],
                                     UnderstandHeader[1]: UnderstandRow[UnderstandHeader[1]],
                                     UnderstandHeader[2]: UnderstandRow[UnderstandHeader[2]],
                                     UnderstandHeader[3]: UnderstandRow[UnderstandHeader[3]],
                                     UnderstandHeader[4]: UnderstandRow[UnderstandHeader[4]],
                                     UnderstandHeader[5]: UnderstandRow[UnderstandHeader[5]],
                                     UnderstandHeader[6]: UnderstandRow[UnderstandHeader[6]],
                                     UnderstandHeader[7]: UnderstandRow[UnderstandHeader[7]],
                                     UnderstandHeader[8]: UnderstandRow[UnderstandHeader[8]],
                                     UnderstandHeader[9]: UnderstandRow[UnderstandHeader[9]],
                                     UnderstandHeader[10]:UnderstandRow[UnderstandHeader[10]],
                                     UnderstandHeader[11]:UnderstandRow[UnderstandHeader[11]],
                                     UnderstandHeader[12]:UnderstandRow[UnderstandHeader[12]],
                                     UnderstandHeader[13]:UnderstandRow[UnderstandHeader[13]],
                                     UnderstandHeader[14]:UnderstandRow[UnderstandHeader[14]],
                                     UnderstandHeader[15]:UnderstandRow[UnderstandHeader[15]],
                                     UnderstandHeader[16]:UnderstandRow[UnderstandHeader[16]],
                                     UnderstandHeader[17]:UnderstandRow[UnderstandHeader[17]],
                                     UnderstandHeader[18]:UnderstandRow[UnderstandHeader[18]],
                                     UnderstandHeader[19]:UnderstandRow[UnderstandHeader[19]],
                                     UnderstandHeader[20]:UnderstandRow[UnderstandHeader[20]],
                                     UnderstandHeader[21]:UnderstandRow[UnderstandHeader[21]],
                                     UnderstandHeader[22]:UnderstandRow[UnderstandHeader[22]],
                                     UnderstandHeader[23]:UnderstandRow[UnderstandHeader[23]],
                                     UnderstandHeader[24]:UnderstandRow[UnderstandHeader[24]],
                                     UnderstandHeader[25]:UnderstandRow[UnderstandHeader[25]],
                                     UnderstandHeader[26]:UnderstandRow[UnderstandHeader[26]],
                                     UnderstandHeader[27]:UnderstandRow[UnderstandHeader[27]],
                                     UnderstandHeader[28]:UnderstandRow[UnderstandHeader[28]],
                                     UnderstandHeader[29]:UnderstandRow[UnderstandHeader[29]],
                                     UnderstandHeader[30]:UnderstandRow[UnderstandHeader[30]],
                                     UnderstandHeader[31]:UnderstandRow[UnderstandHeader[31]],
                                     UnderstandHeader[32]:UnderstandRow[UnderstandHeader[32]],
                                     UnderstandHeader[33]:UnderstandRow[UnderstandHeader[33]],
                                     UnderstandHeader[34]:UnderstandRow[UnderstandHeader[34]],
                                     UnderstandHeader[35]:UnderstandRow[UnderstandHeader[35]],
                                     UnderstandHeader[36]:UnderstandRow[UnderstandHeader[36]],
                                     UnderstandHeader[37]:UnderstandRow[UnderstandHeader[37]],
                                     UnderstandHeader[38]:UnderstandRow[UnderstandHeader[38]],
                                     UnderstandHeader[39]:UnderstandRow[UnderstandHeader[39]],
                                     UnderstandHeader[40]:UnderstandRow[UnderstandHeader[40]],
                                     UnderstandHeader[41]:UnderstandRow[UnderstandHeader[41]],
                                     UnderstandHeader[42]:UnderstandRow[UnderstandHeader[42]],
                                     UnderstandHeader[43]:UnderstandRow[UnderstandHeader[43]],
                                     UnderstandHeader[44]:UnderstandRow[UnderstandHeader[44]],
                                     UnderstandHeader[45]:UnderstandRow[UnderstandHeader[45]],
                                     UnderstandHeader[46]:UnderstandRow[UnderstandHeader[46]],
                                     UnderstandHeader[47]:UnderstandRow[UnderstandHeader[47]],
                                     UnderstandHeader[48]:UnderstandRow[UnderstandHeader[48]],
                                     UnderstandHeader[49]:UnderstandRow[UnderstandHeader[49]],
                                     UnderstandHeader[50]:UnderstandRow[UnderstandHeader[50]],
                                     UnderstandHeader[51]:UnderstandRow[UnderstandHeader[51]],
                                     UnderstandHeader[52]:UnderstandRow[UnderstandHeader[52]],
                                     UnderstandHeader[53]:UnderstandRow[UnderstandHeader[53]],
                                     UnderstandHeader[54]:UnderstandRow[UnderstandHeader[54]],
                                     UnderstandHeader[55]:UnderstandRow[UnderstandHeader[55]],
                                     UnderstandHeader[56]:UnderstandRow[UnderstandHeader[56]],
                                     UnderstandHeader[57]:UnderstandRow[UnderstandHeader[57]],
                                     UnderstandHeader[58]:UnderstandRow[UnderstandHeader[58]],
                                     UnderstandHeader[59]:UnderstandRow[UnderstandHeader[59]],
                                     UnderstandHeader[60]:UnderstandRow[UnderstandHeader[60]],
                                     UnderstandHeader[61]:UnderstandRow[UnderstandHeader[61]],
                                     UnderstandHeader[62]:UnderstandRow[UnderstandHeader[62]],
                                     UnderstandHeader[63]:UnderstandRow[UnderstandHeader[63]],
                                     UnderstandHeader[64]:UnderstandRow[UnderstandHeader[64]],
                                     UnderstandHeader[65]:UnderstandRow[UnderstandHeader[65]],
                                     UnderstandHeader[66]:UnderstandRow[UnderstandHeader[66]],
                                     UnderstandHeader[67]:UnderstandRow[UnderstandHeader[67]],
                                     UnderstandHeader[68]:UnderstandRow[UnderstandHeader[68]],
                                     UnderstandHeader[69]:UnderstandRow[UnderstandHeader[69]],
                                     UnderstandHeader[70]:UnderstandRow[UnderstandHeader[70]],
                                     UnderstandHeader[71]:UnderstandRow[UnderstandHeader[71]],
                                     UnderstandHeader[72]:UnderstandRow[UnderstandHeader[72]],
                                     UnderstandHeader[73]:UnderstandRow[UnderstandHeader[73]],
                                     UnderstandHeader[74]:UnderstandRow[UnderstandHeader[74]],
                                     UnderstandHeader[75]:UnderstandRow[UnderstandHeader[75]]})              
            UnderstandFile.seek(1)            
except IOError:
    print("I/O error")



# Open C:/Users/TungNguyen230893/Desktop/UCI/Winter2019/Inf199/complexityOutput/new_time_17_buggy_classes.csv to read
# Open C:/Users/TungNguyen230893/Desktop/UCI/Winter2019/Inf199/new_time_buggy_db.csv to read
# Open C:/Users/TungNguyen230893/Desktop/UCI/Winter2019/Inf199/merge_pac_understand.csv to write
        # Read headers of new_time_17_buggy_classes.csv and new_time_buggy_db.csv into PacHeader and UnderstandHeader
        # Extend PacHeader using UnderstandHeader and assign the value to MergeFieldHeader
        # Write the MergeFieldHeader into merge_pac_understand
        # For each row in the file new_time_17_buggy_classes
            # For each row in the file new_time_buggy_db
                # if PacHeader['cfg.file'] == UnderstandHeader['Name']
                    # Extend the row of file new_time_17_buggy_classes using new_time_buggy_d and assign it to combine
                    # Write combine into merge_pac_understand.csv
                    
# if PacHeader['cfg.file'] == UnderstandHeader['Name']
    # Extend the row of file new_time_17_buggy_classes using new_time_buggy_d and assign it to combine
    # Write combine into merge_pac_understand.csv                    
# Close merge_pac_understand.csv, new_time_buggy_db.csv, and new_time_17_buggy_classes.csv 
# Don't need to close all files when you open with "with open", you need to close them if you open with "open"
# If you use extend and assign it to the variable that you want to extend, you will get None. None is the returned value 
# of extend method. 
# 4650



#             i = 1
#             while i < count:
#                 PacNameFile = PacRow[PacHeader[1]].strip()
#                 UnderstandNameFile1 = UnderstandContent[i]
#                 UnderstandNameFile      = UnderstandNameFile1[UnderstandHeader[1]].strip()
#                 print(PacNameFile)
#                 print(UnderstandNameFile)
#                 print()
#                 ++i


# To set the pointer to the beginning of the DictRead, we set the file pointer using .seek(0)
#         for PacRow in PacContent:     
#             for UnderstandRow in UnderstandContent:
#                 PacNameFile = PacRow[PacHeader[1]].strip()
#                 UnderstandNameFile = UnderstandRow[UnderstandHeader[1]].strip()
#                 print(PacNameFile)
#                 print(UnderstandNameFile)
#                 print()
#             UnderstandFile.seek(0)

# This is even slower
# Store the value of UnderstandRow in the format of key:value
# Where key is the Name and value is the entire row
#         for UnderstandRow in UnderstandContent:
#             UnderstandNameFile = UnderstandRow[UnderstandHeader[1]].strip()
#             UnderstandDict[UnderstandNameFile] = UnderstandRow
#             print(UnderstandDict)
#76

#                 
#                 if (PacNameFile == UnderstandNameFile):
#                     print(PacNameFile)

#                     MergeRow[:] = []
#                     MergeRow += PacRow
#                     MergeRow += UnderstandRow
#                     writer.writerow(MergeRow) 