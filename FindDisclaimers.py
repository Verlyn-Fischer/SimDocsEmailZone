import csv
import re

def processHashFile(fileName):
    logFile_list = []
    with open(fileName, newline='') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',', quotechar='"')
        rowIndex = 0
        for row in csvReader:
            if rowIndex != 0:
                print(f'Processing File: {rowIndex}')
                totalChanges = loadTextFile(row[2])
                logFile_list.append((row[0],row[2],totalChanges))
            rowIndex +=1
    logFile = 'logFile.csv'

    with open(logFile, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(logFile_list)

def loadTextFile(hashText):
    source = 'original/'
    target = 'modified/'
    totalChanges = 0

    fileName = source + hashText + '.txt'
    f = open(fileName,"r")
    contents = f.read()
    f.close()

    contents, changes = re.subn(pattern=r'This email and(.|\n)*?delete this message', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'Confidentiality Notice(.|\n)*?7B21E720', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'Confidentiality Notice(.|\n)*?is strictly prohibited', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'This e-mail \(including(.|\n)*?Thank you', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'CONFIDENTIALITY NOTICE(.|\n)*?and any attachments', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'This email contains(.|\n)*?is marked CONFIDENTIAL', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'This document and(.|\n)*?the document\(s\)', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'Registered Representative of(.|\n)*?email/disclaimer/', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'Disclaimer: This electronic(.|\n)*?information it contains', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'This e-mail, including(.|\n)*?e-mail immediately', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'The information transmitted(.|\n)*?the original message', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'CONFIDENTIALITY NOTICE(.|\n)*?along with any', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'CONFIDENTIALITY NOTICE(.|\n)*?notify the sender immediately', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'The information transmitted(.|\n)*?material and information', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'CONFIDENTIALITY NOTICE(.|\n)*?the original message', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'Confidentiality Notice(.|\n)*?and delete this message', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'This e-mail, and(.|\n)*?is strictly prohibited', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'Email messages cannot(.|\n)*?of the original message', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'IRS Compliance(.|\n)*?matter addressed herein', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'Confidentiality Notice(.|\n)*?you for your cooperation', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'Notice: The information(.|\n)*?record can be corrected', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'HCSC Company Disclaimer(.|\n)*?6900 in Texas', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'The information contained(.|\n)*?Thank you', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'This email and any files(.|\n)*?and delete this message', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'This e-mail(.|\n)*?then delete it\.\? Thank you', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'This email contains information(.|\n)*?is marked CONFIDENTIAL', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'CONFIDENTIALITY NOTICE: The(.|\n)*?communication and any attachments', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'The information contained in(.|\n)*?of the original message', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'Privacy Notification: This(.|\n)*?Thank you', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'This email and any(.|\n)*?and delete this message', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'Disclaimer: The email(.|\n)*?Surgery Partners, Inc', repl=r'', string=contents)
    totalChanges += changes

    contents, changes = re.subn(pattern=r'CONFIDENTIALITY NOTICE: The(.|\n)*?communication and any attachments', repl=r'', string=contents)
    totalChanges += changes

    # contents, changes = re.subn(pattern=r'TBD(.|\n)*?TBD', repl=r'', string=contents)
    # totalChanges += changes


    fileName = target + hashText + '.txt'
    f2 = open(fileName,"w+")
    f2.write(contents)
    f2.close()

    return totalChanges



def main():
    hashFile = 'Email_Zone_Characterization_ESA_Doc_List.csv'
    processHashFile(hashFile)

main()


