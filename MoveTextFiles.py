import csv
import subprocess

def loadHashFile(fileName):
    with open(fileName, newline='') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in csvReader:
            moveFile(row[2])


def main():
    fileName = 'Email_Zone_Characterization_ESA_Doc_List.csv'
    loadHashFile(fileName)

def moveFile(hashText):

    source = '/disco/data/matters/by_name/ESA_Toxicology/OcrData/'
    target = '/home/fischer/sim_doc_email/original/'
    sourceFilepath = source + hashText[0:4] + '/' + hashText + '.txt'
    targetFilePath = target + hashText + '.txt'

    subprocess.run(["cp", sourceFilepath, targetFilePath])

main()